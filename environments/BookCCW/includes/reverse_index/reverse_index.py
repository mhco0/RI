import includes.common.utils as utils
from includes.common.variable_byte_compression import VariableByteCompression
import includes.database.database as db
from bs4 import BeautifulSoup
import ujson as json
import re
import unidecode
import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class ReverseIndex(object):

    def __init__(self, path_to_database, path_to_extraction_filename, compression):
        self.path_database = path_to_database
        self.extration_filename = path_to_extraction_filename
        self.database = db.Database(self.path_database)
        self.use_compression = compression
        self.doc_id = 0 
        self.dfpostings = {}
        self.path_to_id = {}

        self.__pre_process_attributs()

        if self.use_compression:
            self.__make_compression_postings()
        else:
            self.__make_uncompression_postings()

    def __pre_process_attributs(self):
        pass

    def __make_compression_postings(self):
        dirs = self.database.list_dirs() 
        
        for directory in dirs:
            documents = self.database.load_dir_texts(directory)

            for document in documents:
                self.path_to_id[self.doc_id] = document[1]
                words = self.__tokenize(document[0])

                for word in words: 
                    if word in self.dfpostings:
                        
                        index_range = 0
                        for post_list in self.dfpostings[word]:
                            index_range += VariableByteCompression.decode(post_list[0])

                        if index_range == self.doc_id:
                            self.dfpostings[word][-1][1] += 1
                        else:
                            self.dfpostings[word].append([VariableByteCompression.encode(self.doc_id - index_range), 1])
                            
                    else:
                        self.dfpostings[word] = [[VariableByteCompression.encode(self.doc_id), 1]]

                self.doc_id += 1
    
    def __make_uncompression_postings(self):
        dirs = self.database.list_dirs() 

        for directory in dirs:
            documents = self.database.load_dir_texts(directory)
            
            for document in documents:
                self.path_to_id[self.doc_id] = document[1]
                words = self.__tokenize(document[0])

                for word in words:
                    if word in self.dfpostings:
                        
                        if self.dfpostings[word][-1][0] == self.doc_id:
                            self.dfpostings[word][-1][1] += 1
                        else:
                            self.dfpostings[word].append([self.doc_id, 1])
                    else:
                        self.dfpostings[word] = [[self.doc_id, 1]]

                self.doc_id += 1


    def __tokenize(self, text):
        soup = BeautifulSoup(text, 'html.parser')

        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        html_text = soup.get_text(' ')

        # change characters
        html_text = unidecode.unidecode(html_text)

        # Substitute point and go to lower case
        html_text = re.sub('[^A-Za-z]', ' ', html_text)
        html_text = html_text.lower()
        # tokenize
        tokenized_text = word_tokenize(html_text)
        for word in tokenized_text:
            if word in stopwords.words('portuguese'):
                tokenized_text.remove(word)

            # s_text = " ".join(tokenized_text)

        #print(tokenized_text)
        return tokenized_text

    def get_postings_dict(self):
        return self.dfpostings

    def does_compression(self):
        return self.use_compression

    def get_document_map(self):
        return self.path_to_id

    def get_document_by_id(self, idx):
        if idx in self.path_to_id:
            return self.path_to_id[idx]
        else:
            return ''

    @staticmethod
    def save(index_obj, filename):
        pickle.dump(index_obj, open(filename, "wb"))

    @staticmethod
    def load(filename):
        index_obj = pickle.load(open(filename, "rb"))
        
        return index_obj
