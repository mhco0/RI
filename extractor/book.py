class Book:
    def __init__(self, author, publisher, isbn, language, domain):
        # self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.language = language
        self.domain = domain

    def __str__(self):
        return f'Author: {self.author}\nPublisher: {self.publisher}\nIsbn: {self.isbn}\nLanguage: {self.language}\n'
