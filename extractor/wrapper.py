from bs4 import BeautifulSoup
from book import Book
from utils import Utils

BOOKS_PATH = '../books/'

metaInfo = ['autor', 'isbn', 'ean13', 'isbn-13', 'editora', 'marca', 'idioma']


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
        text: str = res.text
        if (text.lower() in metaInfo):
            book[text] = allTags[index+1].text
    book['domain'] = directory
    return book


books = getAllBooks()
Utils.writeJsonFile('./wrapper_result.json', books)

# htmlPage = Utils.readFile(BOOKS_PATH + 'vila' + '/1.html')
# soup = BeautifulSoup(htmlPage, 'html.parser')
# table = soup.table
# print(table.prettify())
