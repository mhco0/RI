from typing import Match
from book import Book
from utils import Utils
from bs4 import BeautifulSoup

BOOKS_PATH = '../books/'
REGEX_GROUP = '(.+?)'


def createBook(page, preffix: dict, suffix) -> Book:
    author = Utils.regexSearch(
        preffix['author']+REGEX_GROUP+suffix['author'], page)
    publisher = Utils.regexSearch(
        preffix['publisher']+REGEX_GROUP+suffix['publisher'], page)
    isbn = Utils.regexSearch(
        preffix['isbn']+REGEX_GROUP+suffix['isbn'], page)
    language = Utils.regexSearch(
        preffix['language']+REGEX_GROUP+suffix['language'], page)

    return Book(author, publisher, isbn, language)


def americanasWrapper(page) -> Book:
    preffix = {
        'author': 'Autor</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'publisher': 'Editora</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'isbn': 'ISBN-13</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'language': 'Idioma</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
    }

    suf = '</td></tr>'
    suffix = {
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf,
    }

    book = createBook(page, preffix, suffix)
    return book


def shoptimeWrapper(page) -> Book:
    preffix = {
        'author': 'Autor</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'publisher': 'Editora</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'isbn': 'ISBN-13</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'language': 'Idioma</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
    }

    suf = '</td></tr>'
    suffix = {
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf,
    }

    book = createBook(page, preffix, suffix)
    return book


def submarinoWrapper(page) -> Book:
    preffix = {
        'author': 'Autor</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'publisher': 'Editora</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'isbn': 'ISBN-13</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'language': 'Idioma</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
    }

    suf = '</td></tr>'
    suffix = {
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf,
    }

    book = createBook(page, preffix, suffix)
    return book


def curitibaWrapper(page) -> Book:
    preffix = {
        'author': 'Autor</th><td class="value-field Autor">',
        'publisher': 'Editora</th><td class="value-field Editora">',
        'isbn': 'ISBN</th><td class="value-field ISBN">',
        'language': 'Idioma</th><td class="value-field Idioma">'
    }

    suf = '</td></tr>'
    suffix = {
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf
    }

    book = createBook(page, preffix, suffix)
    return book


def vilaWrapper(page) -> Book:
    preffix = {
        'author': 'Autor</th><td class="value-field Autor">',
        'publisher': 'Editora</th><td class="value-field Editora">',
        'isbn': 'ISBN</th><td class="value-field ISBN">',
        'language': 'Idioma</th><td class="value-field Idioma">'
    }

    suf = '</td></tr>'
    suffix = {
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf
    }

    book = createBook(page, preffix, suffix)
    return book


def magazineWrapper(page) -> Book:
    preffix = {
        'author': 'Autor</td> <td class="description__information-right">     <table class="description__box"> <tbody><tr> <td class="description__information-box-left">   </td> <td class="description__information-box-right">',
        'publisher': 'Marca</td> <td class="description__information-right">     <table class="description__box"> <tbody><tr> <td class="description__information-box-left">   </td> <td class="description__information-box-right">',
        'isbn': 'ISBN</td> <td class="description__information-right">     <table class="description__box"> <tbody><tr> <td class="description__information-box-left">   </td> <td class="description__information-box-right">',
        'language': 'Idioma</td> <td class="description__information-right">     <table class="description__box"> <tbody><tr> <td class="description__information-box-left">   </td> <td class="description__information-box-right">'
    }

    suf = '(\n|</td> </tr>)'
    suffix = {
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf
    }

    book = createBook(page, preffix, suffix)

    if book.author == '':
        publisherAuthor = 'Autor </td> <td class="description__information-box-right">(.+?)(\n|</td> </tr>)'
        book.author = Utils.regexSearch(publisherAuthor, page)

    if book.publisher == '':
        publisherAlternative = 'Editora </td> <td class="description__information-box-right">(.+?)</td> </tr>'
        book.publisher = Utils.regexSearch(publisherAlternative, page)

    if book.isbn == '':
        isbnAlternative = 'ISBN-13 -(.+?)</td> </tr>'
        book.isbn = Utils.regexSearch(isbnAlternative, page)
        if book.isbn == '':
            isbnAlternative = 'GTIN-13 -(.+?)</td> </tr>'
            book.isbn = Utils.regexSearch(isbnAlternative, page)

    if book.language == '':
        languageAlternative = 'Idioma </td> <td class="description__information-box-right">(.+?)</td> </tr>'
        book.language = Utils.regexSearch(languageAlternative, page)

    return book


def mercadoLivreWrapper(page) -> Book:
    preffix = {
        'author': 'Autor</th><td class="andes-table__column andes-table__column--left ui-pdp-specs__table__column"><span class="andes-table__column--value">',
        'publisher': 'Editora do livro</th><td class="andes-table__column andes-table__column--left ui-pdp-specs__table__column"><span class="andes-table__column--value">',
        'isbn': 'ISBN</span>:',
        'language': 'Idioma</th><td class="andes-table__column andes-table__column--left ui-pdp-specs__table__column"><span class="andes-table__column--value">'
    }

    suf = '</span></td></tr>'
    suffix = {
        'author': suf,
        'publisher': suf,
        'isbn': '</p></li>',
        'language': suf
    }

    book = createBook(page, preffix, suffix)
    return book


def saraivaWrapper(page) -> Book:
    preffix = {
        'author': '<td class="pl-0">Autor</td>\n                                <td>',
        'publisher': '<td class="pl-0">Marca</td>\n                                <td>',
        'isbn': '<td class="pl-0">ISBN</td>\n                                <td>',
        'language': '<td class="pl-0">Idioma</td>\n                                <td>'
    }

    suf = '</td>'
    suffix = {
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf
    }

    book = createBook(page, preffix, suffix)
    return book


def travessaWrapper(page) -> Book:
    preffix = {
        'author': 'autor: <a href=(?:.+?) class="txtConteudo">',
        'publisher': 'editora: <a href=(?:.+?) font="" class="txtConteudo">',
        'isbn': '<span id="lblDadosIsbn" class="txtDescricao">',
        'language': '<span id="lblDadosIdioma" class="txtDescricao">'
    }

    suf = '<br></span>'
    suffix = {
        'author': '</a>',
        'publisher': '</a>',
        'isbn': suf,
        'language': suf
    }

    book = createBook(page, preffix, suffix)
    return book


def culturaWrapper(page) -> Book:
    preffix = {
        'author': '<span>Autor</span><span>',
        'publisher': '<span>Editora: </span><h2><(?:.+?)><a(?:.+?)>',
        'isbn': '<span>ISBN</span><span>',
        'language': '<span>Idioma</span><span>'
    }

    suf = '</span>'
    suffix = {
        'author': suf,
        'publisher': '</a></div></h2>',
        'isbn': suf,
        'language': suf
    }

    book = createBook(page, preffix, suffix)
    return book


def singleWrapper(page) -> Book:

    soup = BeautifulSoup(page, 'html.parser')
    authorInfo = ['autor', 'autor:']
    isbnInfo = ['isbn', 'ean13', 'isbn-13', 'isbn:', 'código do produto']
    publisherInfo = ['editora', 'marca', 'editora do livro', 'editora:']
    languageInfo = ['idioma', 'idioma:']

    author = ""
    publisher = ""
    isbn = ""
    language = ""

    allTags = soup.find_all('a', href=True)
    for index, res in enumerate(allTags):
        link = res['href']
        if '/autor/' in link:
            author = res.text
        if '/editora/' in link:
            publisher = res.text

    allTags = soup.find_all(["th", "td", "span", "a"])
    for index, res in enumerate(allTags):
        text: str = res.text.lower().strip()
        if (text in authorInfo):
            author = allTags[index+1].text
        elif (text in publisherInfo):
            publisher = allTags[index+1].text
        elif (text in isbnInfo):
            isbn = allTags[index+1].text.strip()
            if len(isbn) > 13:
                isbn = isbn.split(' ')[-1]
        elif (text in languageInfo):
            language = allTags[index+1].text

    return Book(author, publisher, isbn, language)


def getAllBooks(option):
    print("getting books...")
    directories = ['americanas', 'cultura', 'curitiba', 'magazine',
                   'mercadoLivre', 'saraiva', 'shoptime', 'submarino', 'travessa', 'vila']
    wrappers = {
        'americanas': americanasWrapper,
        'cultura': culturaWrapper,
        'curitiba': curitibaWrapper,
        'magazine': magazineWrapper,
        'mercadoLivre': mercadoLivreWrapper,
        'saraiva': saraivaWrapper,
        'shoptime': shoptimeWrapper,
        'submarino': submarinoWrapper,
        'travessa': travessaWrapper,
        'vila': vilaWrapper
    }
    books = []
    for directory in directories:
        filenames = Utils.getFilenames(BOOKS_PATH + directory + '/pos')
        for filename in filenames:
            page = Utils.readFile(
                BOOKS_PATH + directory + '/pos' + f'/{filename}')
            data = wrappers[directory](page) if (
                option == 1) else singleWrapper(page)
            book = {
                'author': data.author.strip(),
                'publisher': data.publisher.strip(),
                'isbn': data.isbn.strip(),
                'language': data.language.strip(),
                'domain': directory

            }
            books.append(book)
    return books


def writeBooks(books):
    Utils.writeJsonFile('./result.json', books)


def menu():
    userInput = ''
    while(userInput != '3'):
        print("Choose an option:")
        print("1 - Individual wrappers")
        print("2 - Single wrapper")
        print("3 - exit")
        userInput = input("option:")
        if userInput == '1':
            books = getAllBooks(1)
            Utils.writeJsonFile('./result.json', books)
            break
        elif userInput == '2':
            books = getAllBooks(2)
            Utils.writeJsonFile('./single_result.json', books)
            break
        elif userInput == '3':
            break
        else:
            print("Invalid option, try again!")


menu()
