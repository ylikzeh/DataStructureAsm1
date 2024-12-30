class Book:
    def __init__(self, isbn, name, author, year, publisher):
        self.isbn = isbn  # ISBN is a string
        self.name = name
        self.author = author
        self.year = year
        self.publisher = publisher

    def __repr__(self):
        return f"Book(ISBN: {self.isbn}, Name: {self.name})"