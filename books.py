class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class Bookcase:
    def __init__(self, books=None):
        self.books = books

    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for author, title in book_list:
            books.append(Book(author, title))
            return cls(books)


