from models import Book
from storage import Storage

class BookManager:
    def __init__(self):
        self.storage = Storage('books.json')
        self.books = self.storage.load_data()

    def add_book(self, title, author, isbn):
        #check if the book already exists before adding
        if any(book['isbn'] == isbn for book in self.books):
            print("Book with this ISBN already exists.")
            return
        new_book = Book(title, author, isbn)
        self.books.append(new_book.__dict__)
        self.storage.save_data(self.books)
        print(f"Added: {new_book.title}")

    def update_book(self, isbn, new_title=None, new_author=None):
        #update the book's title and author if it exists
        for book in self.books:
            if book['isbn'] == isbn:
                if new_title:
                    book['title'] = new_title
                if new_author:
                    book['author'] = new_author
                self.storage.save_data(self.books)
                print(f"Updated book with ISBN: {isbn}")
                return
        print("Book not found.")

    def delete_book(self, isbn):
        #remove the book if it exists
        original_count = len(self.books)
        self.books = [book for book in self.books if book['isbn'] != isbn]
        if len(self.books) < original_count:
            self.storage.save_data(self.books)
            print(f"Deleted book with ISBN: {isbn}")
        else:
            print("Book not found.")

    def list_books(self):
        #print all books in the system
        for book in self.books:
            print(book)

    def search_books(self, title=None, author=None, isbn=None):
        #find books matching the search criteria
        results = [
            book for book in self.books
            if (title and title.lower() in book['title'].lower()) or
               (author and author.lower() in book['author'].lower()) or
               (isbn and book['isbn'] == isbn)
        ]
        if results:
            for book in results:
                print(Book(**book))
        else:
            print("No matching books found.")
