from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from utils import Utils
import re
import unidecode
# Remove stopwords
import nltk
from mutual_information import MutualInformation
nltk.download('punkt')

nltk.download('stopwords')

BOOKS_PATH = '../books/'
DOMAINS = ['americanas', 'cultura', 'curitiba', 'magazine',
           'mercadoLivre', 'saraiva', 'shoptime', 'submarino', 'travessa', 'vila']


def tokenize(text):
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

    # text = " ".join(tokenized_text)

    return tokenized_text


print('getting text...')
list_corpus = []
for directory in DOMAINS:
    filenames = Utils.getFilenames(BOOKS_PATH + directory + '/pos')
    for filename in filenames:
        filePath = BOOKS_PATH + directory + '/pos' + f'/{filename}'
        page = Utils.readFile(filePath)
        data = tokenize(page)
        list_corpus += data

print('writting text...')
Utils.writeJsonFile('./static/list_corpus.txt', list_corpus)
