class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully")

    def display_books(self):
        print("\nAvailable Books:")

        if len(self.books) == 0:
            print("No books available")
        else:
            for book in self.books:
                print(book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully")
        else:
            print("Book not available")

library = Library()

library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Machine Learning")

library.display_books()

library.issue_book("Python Programming")

library.display_books()