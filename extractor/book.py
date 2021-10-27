class Book:
    def __init__(self, author, publisher, isbn, date):
        # self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        # self.language = language
        self.date = date

    def __str__(self):
        return f'Author: {self.author}\nPublisher: {self.publisher}\nIsbn: {self.isbn}\nDate: {self.date}\n'
