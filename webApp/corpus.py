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


def pageToResult(page: str):
    url = Utils.regexSearch('saved from url=\(\d\d\d\d\)(.+?) -->', page)
    soup = BeautifulSoup(page, 'html.parser')
    head = soup.head

    title = head.title
    description = ''
    if title:
        title = title.text
    else:
        'Sem Titulo'
    metas = head.find_all('meta')
    for meta in metas:
        if meta.has_attr('name'):
            if meta['name'] == 'description':
                description = meta['content']
                break

    return [title, description, url]


paths = Utils.readJsonFile('./paths.json')

print('getting text...')
results = {}
for id, path in paths.items():
    page = Utils.readFile(path)
    result = pageToResult(page)
    results[id] = result

print('writting text...')
Utils.writeJsonFile('./results.json', results)
