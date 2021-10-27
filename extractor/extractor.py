from book import Book
from utils import Utils

BOOKS_PATH = '../books/'
REGEX_GROUP = '(.+?)'


def createBook(page, preffix: dict, suffix) -> Book:
    # title = Utils.regexSearch(preffix['title']+REGEX_GROUP+suffix['title'], page)
    author = Utils.regexSearch(
        preffix['author']+REGEX_GROUP+suffix['author'], page)
    publisher = Utils.regexSearch(
        preffix['publisher']+REGEX_GROUP+suffix['publisher'], page)
    isbn = Utils.regexSearch(
        preffix['isbn']+REGEX_GROUP+suffix['isbn'], page)
    language = Utils.regexSearch(
        preffix['language']+REGEX_GROUP+suffix['language'], page)
    # date = Utils.regexSearch(preffix['date']+REGEX_GROUP+suffix['date'], page)

    return Book(author, publisher, isbn, language)


def americanasWrapper(page) -> Book:
    preffix = {
        # 'title': 'Título</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'author': 'Autor</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'publisher': 'Editora</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'isbn': 'ISBN-13</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        'language': 'Idioma</td><td class="src__Text-sc-70o4ee-7 iHQLKS">',
        # 'date': 'Data de publicação</td><td class="src__Text-sc-70o4ee-7 iHQLKS">'
    }

    suf = '</td></tr>'
    suffix = {
        # 'title': suf,
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf,
        # 'date': suf
    }

    book = createBook(page, preffix, suffix)
    return book


def shoptimeWrapper(page) -> Book:
    preffix = {
        # 'title': 'Título</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'author': 'Autor</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'publisher': 'Editora</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'isbn': 'ISBN-13</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        'language': 'Idioma</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">',
        # 'date': 'Data de publicação</td><td class="src__Text-sc-1m6tc2l-4 kBDbsy">'
    }

    suf = '</td></tr>'
    suffix = {
        # 'title': suf,
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf,
        # 'date': suf
    }

    book = createBook(page, preffix, suffix)
    return book


def submarinoWrapper(page) -> Book:
    preffix = {
        # 'title': 'Título</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'author': 'Autor</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'publisher': 'Editora</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'isbn': 'ISBN-13</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        'language': 'Idioma</td><td class="src__Text-sc-10qje1m-4 fyapQy">',
        # 'date': 'Data de publicação</td><td class="src__Text-sc-10qje1m-4 fyapQy">'
    }

    suf = '</td></tr>'
    suffix = {
        # 'title': suf,
        'author': suf,
        'publisher': suf,
        'isbn': suf,
        'language': suf,
        # 'date': suf
    }

    book = createBook(page, preffix, suffix)
    return book


def curitibaWrapper(page) -> Book:
    preffix = {
        'author': 'Autor</th><td class="value-field Autor">',
        'publisher': 'Editora</th><td class="value-field Editora">',
        'isbn': 'EAN13</th><td class="value-field EAN13">',
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

    if book.publisher == '':
        publisherAlternative = 'Editora </td> <td class="description__information-box-right">(.+?)</td> </tr>'
        book.publisher = Utils.regexSearch(publisherAlternative, page)

    if book.isbn == '':
        isbnAlternative = 'ISBN-13 -(.+?)</td> </tr>'
        book.isbn = Utils.regexSearch(isbnAlternative, page)

    if book.language == '':
        languageAlternative = 'Idioma </td> <td class="description__information-box-right">(.+?)</td> </tr>'
        book.language = Utils.regexSearch(languageAlternative, page)

    return book


def mercadoLivreWrapper(page) -> Book:
    preffix = {
        'author': 'Autor</th><td class="andes-table__column andes-table__column--left ui-pdp-specs__table__column"><span class="andes-table__column--value">',
        'publisher': 'Editora</th><td class="andes-table__column andes-table__column--left ui-pdp-specs__table__column"><span class="andes-table__column--value">',
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


def listAllBooks():
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
    for directory in directories:
        print(
            f'------------------- {directory.capitalize()} -----------------')
        filenames = Utils.getFilenames(BOOKS_PATH + directory)
        for filename in filenames:
            page = Utils.readFile(BOOKS_PATH + directory + f'/{filename}')
            print(wrappers[directory](page))
        print(f'------------------------------------------\n')


listAllBooks()
