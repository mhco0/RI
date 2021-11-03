from bs4 import BeautifulSoup
from book import Book
from utils import Utils

BOOKS_PATH = '../books/'

authorInfo = ['autor']
isbnInfo = ['isbn', 'ean13', 'isbn-13', ]
publisherInfo = ['editora', 'marca']
languageInfo = ['idioma']


def getAllBooks() -> list:
    print("getting books...")
    books = []

    directories = ['americanas', 'cultura', 'curitiba', 'magazine',
                   'mercadoLivre', 'saraiva', 'shoptime', 'submarino', 'travessa', 'vila']
    for directory in directories:
        filenames = Utils.getFilenames(BOOKS_PATH + directory)
        for filename in filenames:
            htmlPage = Utils.readFile(BOOKS_PATH + directory + f'/{filename}')
            soup = BeautifulSoup(htmlPage, 'html.parser')
            books.append(wrapper(soup, directory))
    return books


def wrapper(soup: BeautifulSoup, directory: str) -> dict:
    book = {}
    allTags = soup.find_all(["th", "td"])
    for index, res in enumerate(allTags):
        text: str = res.text.lower().strip()
        if (text in authorInfo):
            book['author'] = allTags[index+1].text
        elif (text in publisherInfo):
            book['publisher'] = allTags[index+1].text
        elif (text in isbnInfo):
            book['isbn'] = allTags[index+1].text
        elif (text in languageInfo):
            book['language'] = allTags[index+1].text

    book['domain'] = directory
    return book


books = getAllBooks()
Utils.writeJsonFile('./wrapper_result.json', books)
