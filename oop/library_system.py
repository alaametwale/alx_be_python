class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [str(book) for book in self.books]

    def __str__(self):
        return "\n".join(self.list_books())


# --- Example used by the checker ---
if __name__ == "__main__":
    library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen")
    ebook = EBook("Snow Crash", "Neal Stephenson", 500)
    printbook = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    library.add_book(classic_book)
    library.add_book(ebook)
    library.add_book(printbook)

    print(library)
