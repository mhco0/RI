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
        self.dfattributes = {}
        self.path_to_id = {}

        if self.use_compression:
            self.__pre_process_attributes_compression()
            self.__make_compression_postings()
        else:
            self.__pre_process_attributes_uncompression()
            self.__make_uncompression_postings()

    def __pre_process_attributes_compression(self):
        with open(self.extration_filename, 'r') as file:
            data = json.load(file)

        extract_info = ["author", "publisher", "language", "domain"]

        for pair_att_value in data:
            self.path_to_id[self.doc_id] = self.path_database + '/' + pair_att_value["path"]

            isbn = pair_att_value["isbn"]

            word = "isbn." + isbn

            if word in self.dfattributes:
                index_range = 0
                for post_list in self.dfattributes[word]:
                    index_range += VariableByteCompression.decode(post_list[0])

                if index_range == self.doc_id:
                    self.dfattributes[word][-1][1] += 1
                else:
                    self.dfattributes[word].append([VariableByteCompression.encode(self.doc_id - index_range), 1])
                    
            else:
                self.dfattributes[word] = [[VariableByteCompression.encode(self.doc_id), 1]]

            for info in extract_info:
                words = self.__tokenize(pair_att_value[info])

                for word in words:
                    word = info + '.' + word
                    if word in self.dfattributes:
                        index_range = 0
                        for post_list in self.dfattributes[word]:
                            index_range += VariableByteCompression.decode(post_list[0])

                        if index_range == self.doc_id:
                            self.dfattributes[word][-1][1] += 1
                        else:
                            self.dfattributes[word].append([VariableByteCompression.encode(self.doc_id - index_range), 1])
                            
                    else:
                        self.dfattributes[word] = [[VariableByteCompression.encode(self.doc_id), 1]]


            self.doc_id += 1

            
    def __pre_process_attributes_uncompression(self):
        with open(self.extration_filename, 'r') as file:
            data = json.load(file)

        extract_info = ["author", "publisher", "language", "domain"]

        for pair_att_value in data:
            self.path_to_id[self.doc_id] = self.path_database + '/' + pair_att_value["path"]

            isbn = pair_att_value["isbn"]

            word = "isbn." + isbn

            if word in self.dfattributes:
                if int.from_bytes(self.dfattributes[word][-1][0], 'little') == self.doc_id:
                    self.dfattributes[word][-1][1] += 1
                else:
                    self.dfattributes[word].append([bytearray(self.doc_id.to_bytes(4, 'little')), 1])
            else:
                self.dfattributes[word] = [[bytearray(self.doc_id.to_bytes(4, 'little')), 1]]

            for info in extract_info:
                words = self.__tokenize(pair_att_value[info])

                for word in words:
                    word = info + '.' + word
                    if word in self.dfattributes:
                        if int.from_bytes(self.dfattributes[word][-1][0], 'little') == self.doc_id:
                            self.dfattributes[word][-1][1] += 1
                        else:
                            self.dfattributes[word].append([bytearray(self.doc_id.to_bytes(4, 'little')), 1])
                            
                    else:
                        self.dfattributes[word] = [[bytearray(self.doc_id.to_bytes(4, 'little')), 1]]


            self.doc_id += 1

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
                        
                        if int.from_bytes(self.dfpostings[word][-1][0], 'little') == self.doc_id:
                            self.dfpostings[word][-1][1] += 1
                        else:
                            self.dfpostings[word].append([bytearray(self.doc_id.to_bytes(4, 'little')), 1])
                    else:
                        self.dfpostings[word] = [[bytearray(self.doc_id.to_bytes(4, 'little')), 1]]

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

    def get_attributes_map(self):
        return self.dfattributes

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
