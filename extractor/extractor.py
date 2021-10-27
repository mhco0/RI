from book import Book
from utils import Utils

BOOKS_PATH = '../books/'


def createBook(page, preffix: dict, suffix) -> Book:
    # title = Utils.regexSearch(preffix['title']+'(.+?)'+suffix['title'], page)
    author = Utils.regexSearch(
        preffix['author']+'(.+?)'+suffix['author'], page)
    publisher = Utils.regexSearch(
        preffix['publisher']+'(.+?)'+suffix['publisher'], page)
    isbn = Utils.regexSearch(preffix['isbn']+'(.+?)'+suffix['isbn'], page)
    # language = Utils.regexSearch(
    # # preffix['language']+'(.+?)'+suffix['language'], page)
    date = Utils.regexSearch(preffix['date']+'(.+?)'+suffix['date'], page)

    return Book(author, publisher, isbn, date)


def americanasWrapper(page) -> Book:
    preffix = {
        # 'title': 'Título</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'author': 'Autor</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'publisher': 'Editora</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'isbn': 'ISBN-13</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        # 'language': 'Idioma</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'date': 'Data de publicação</td><td class="src__Text-sc-70o4ee-7 iHQLKS">'
    }

    suffix = {
        # 'title': '</td></tr>',
        'author': '</td></tr>',
        'publisher': '</td></tr>',
        'isbn': '</td></tr>',
        # 'language': '</td></tr>',
        'date': '</td></tr>'
    }

    book = createBook(page, preffix, suffix)
    return book


def shoptimeWrapper(page) -> Book:
    preffix = {
        # 'title': 'Título</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'author': 'Autor</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'publisher': 'Editora</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'isbn': 'ISBN-13</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        # 'language': 'Idioma</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'date': 'Data de publicação</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">'
    }

    suffix = {
        # 'title': '</td></tr>',
        'author': '</td></tr>',
        'publisher': '</td></tr>',
        'isbn': '</td></tr>',
        # 'language': '</td></tr>',
        'date': '</td></tr>'
    }

    book = createBook(page, preffix, suffix)
    return book


def submarinoWrapper(page) -> Book:
    preffix = {
        # 'title': 'Título</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'author': 'Autor</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'publisher': 'Editora</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'isbn': 'ISBN-13</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        # 'language': 'Idioma</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'date': 'Data de publicação</td><td class="src__Text-sc-10qje1m-4 fyapQy">'
    }

    suffix = {
        # 'title': '</td></tr>',
        'author': '</td></tr>',
        'publisher': '</td></tr>',
        'isbn': '</td></tr>',
        # 'language': '</td></tr>',
        'date': '</td></tr>'
    }

    book = createBook(page, preffix, suffix)
    return book


def listAllBooks():
    directories = ['americanas', 'shoptime', 'submarino']
    wrappers = {
        'americanas': americanasWrapper,
        'shoptime': shoptimeWrapper,
        'submarino': submarinoWrapper
    }
    for directory in directories:
        print(
            f'------------------- {directory.capitalize()} -----------------')
        filenames = Utils.getFilenames(BOOKS_PATH + directory)
        for filename in filenames:
            page = Utils.readFile(BOOKS_PATH + directory + f'/{filename}')
            print(wrappers[directory](page))
        print(f'------------------------------------------\n')


listAllBooks()
