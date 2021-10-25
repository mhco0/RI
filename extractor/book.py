class Book:
    def __init__(self, title, author, publisher, isbn, language, date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.language = language
        self.date = date

    def __str__(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\nIsbn: {self.isbn}\nLanguage: {self.language} \nDate: {self.date}\n'
