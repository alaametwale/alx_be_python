class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


class PrintBook(Book):
    def __init__(self, title, author, year, page_count):
        super().__init__(title, author, year)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author} ({self.year}) - {self.page_count} pages"


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author} ({self.year}) - {self.file_size}MB"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [str(book) for book in self.books]

    def __str__(self):
        return "\n".join(self.list_books())


# Example output for checker
if __name__ == "__main__":
    library = Library()

    p1 = PrintBook("1984", "George Orwell", 1949, 328)
    e1 = EBook("Python Basics", "Alaa Meto", 2024, 5)

    library.add_book(p1)
    library.add_book(e1)

    print(library)
