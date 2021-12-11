from typing import Match
from book import Book
from utils import Utils
from bs4 import BeautifulSoup

BOOKS_PATH = '../books/'
REGEX_GROUP = '(.+?)'
DOMAINS = ['americanas', 'cultura', 'curitiba', 'magazine',
           'mercadoLivre', 'saraiva', 'shoptime', 'submarino', 'travessa', 'vila']


def bookToDict(book: tuple):
    return {
        'author': book[0].author,
        'publisher': book[0].publisher,
        'isbn': book[0].isbn,
        'language': book[0].language,
        'domain': book[0].domain,
        'path': book[1]
    }


def createBook(page, domain, preffix: dict, suffix) -> Book:
    author = Utils.regexSearch(
        preffix['author']+REGEX_GROUP+suffix['author'], page).strip()
    publisher = Utils.regexSearch(
        preffix['publisher']+REGEX_GROUP+suffix['publisher'], page).strip()
    isbn = Utils.regexSearch(
        preffix['isbn']+REGEX_GROUP+suffix['isbn'], page).strip()
    language = Utils.regexSearch(
        preffix['language']+REGEX_GROUP+suffix['language'], page).strip()

    return Book(author, publisher, isbn, language, domain)


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

    book = createBook(page, 'americanas', preffix, suffix)
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

    book = createBook(page, 'shoptime', preffix, suffix)
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

    book = createBook(page, 'submarino', preffix, suffix)
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

    book = createBook(page, 'curitiba', preffix, suffix)
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

    book = createBook(page, 'vila', preffix, suffix)
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

    book = createBook(page, 'magazine', preffix, suffix)

    if book.author == '':
        publisherAuthor = 'Autor </td> <td class="description__information-box-right">(.+?)(\n|</td> </tr>)'
        book.author = Utils.regexSearch(publisherAuthor, page).strip()

    if book.publisher == '':
        publisherAlternative = 'Editora </td> <td class="description__information-box-right">(.+?)</td> </tr>'
        book.publisher = Utils.regexSearch(publisherAlternative, page).strip()

    if book.isbn == '':
        isbnAlternative = 'ISBN-13 -(.+?)</td> </tr>'
        book.isbn = Utils.regexSearch(isbnAlternative, page).strip()
        if book.isbn == '':
            isbnAlternative = 'GTIN-13 -(.+?)</td> </tr>'
            book.isbn = Utils.regexSearch(isbnAlternative, page).strip()

    if book.language == '':
        languageAlternative = 'Idioma </td> <td class="description__information-box-right">(.+?)</td> </tr>'
        book.language = Utils.regexSearch(languageAlternative, page).strip()

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

    book = createBook(page, 'mercadoLivre', preffix, suffix)
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

    book = createBook(page, 'saraiva', preffix, suffix)
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

    book = createBook(page, 'travessa', preffix, suffix)
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

    book = createBook(page, 'cultura', preffix, suffix)
    return book


def checkIsbn(isbn: str):
    if len(isbn) > 13:
        temp = isbn.split(' ')
        isbn = ''
        for result in temp:
            if len(result) == 13:
                isbn = result

    return isbn if len(isbn) >= 10 else ''


def singleWrapper(page, domain) -> Book:

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
            author = allTags[index+1].text.strip()
        elif (text in publisherInfo):
            publisher = allTags[index+1].text.strip()
        elif (text in isbnInfo):
            isbn = checkIsbn(allTags[index+1].text.strip())
        elif (text in languageInfo):
            language = allTags[index+1].text.strip()

    return Book(author, publisher, isbn, language, domain)


def getAllBooks(option):
    print('getting books...')
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
    for directory in DOMAINS:
        filenames = Utils.getFilenames(BOOKS_PATH + directory + '/pos')
        for filename in filenames:
            filePath = BOOKS_PATH + directory + '/pos' + f'/{filename}'
            page = Utils.readFile(filePath)
            data = wrappers[directory](page) if (
                option == 'manual') else singleWrapper(page, directory)
            books.append((data, filePath))
    return books


def evalMetrics(n, e, c):
    if c == 0 or e == 0:
        return (0, 0, 0)

    recall = c/n
    precision = c/e
    fMeasure = 2*recall*precision/(recall+precision)
    return (recall, precision, fMeasure)


def measureBooks(refBooks: list[Book], extractBooks: list[Book]):
    e = 0
    c = 0
    n = len(refBooks) * 4
    for index, book in enumerate(extractBooks):
        if book.author != '':
            e = e + 1
            if book.author == refBooks[index].author:
                c = c + 1
        if book.publisher != '':
            e = e + 1
            if book.publisher == refBooks[index].publisher:
                c = c + 1
        if book.isbn != '':
            e = e + 1
            if book.isbn == refBooks[index].isbn:
                c = c + 1
        if book.language != '':
            e = e + 1
            if book.language == refBooks[index].language:
                c = c + 1

    return (n, e, c)


def calcAllMetrics(manualBooks: list[Book], singleWrapperBooks: list[Book]):
    print('calculating metrics...')
    metrics = []
    nT = 0
    eT = 0
    cT = 0
    for domain in DOMAINS:
        refBooks = [book for book in manualBooks if book.domain == domain]
        extractBooks = [
            book for book in singleWrapperBooks if book.domain == domain]
        n, e, c = measureBooks(refBooks, extractBooks)
        recall, precision, fMeasure = evalMetrics(n, e, c)
        nT = nT + n
        eT = eT + e
        cT = cT + c
        metrics.append({
            'n': n,
            'e': e,
            'c': c,
            'recall': recall,
            'precision': precision,
            'f-Measure': fMeasure,
            'domain': domain
        })
    recall, precision, fMeasure = evalMetrics(nT, eT, cT)
    metrics.append({
        'n': nT,
        'e': eT,
        'c': cT,
        'recall': recall,
        'precision': precision,
        'f-Measure': fMeasure,
        'domain': 'all'
    })
    Utils.writeJsonFile('./metricsV3.json', metrics)


def main():
    manualBooks = getAllBooks('manual')
    books = list(map(bookToDict, manualBooks))
    Utils.writeJsonFile('./data.json', books)

    # singleWrapperBooks = getAllBooks('single')
    # books = list(map(bookToDict, singleWrapperBooks))
    # Utils.writeJsonFile('./single_resultV3.json', books)

    # calcAllMetrics(manualBooks, singleWrapperBooks)


main()
