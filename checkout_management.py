from storage import Storage

class CheckoutManager:
    def __init__(self):
        self.book_storage = Storage('books.json')
        self.checkout_storage = Storage('checkouts.json')
        self.books = self.book_storage.load_data()
        self.checkouts = self.checkout_storage.load_data()

    def checkout_book(self, user_id, isbn):
        #check out a book if it is available
        for book in self.books:
            if book['isbn'] == isbn and book['available']:
                book['available'] = False
                self.checkouts.append({"user_id": user_id, "isbn": isbn})
                self.book_storage.save_data(self.books)
                self.checkout_storage.save_data(self.checkouts)
                print(f"Checked out book with ISBN: {isbn} to user {user_id}")
                return
        print("Book not available or invalid ISBN.")

    def checkin_book(self, isbn):
        #check in a book if it was checked out
        for book in self.books:
            if book['isbn'] == isbn and not book['available']:
                book['available'] = True
                self.checkouts = [c for c in self.checkouts if c['isbn'] != isbn]
                self.book_storage.save_data(self.books)
                self.checkout_storage.save_data(self.checkouts)
                print(f"Checked in book with ISBN: {isbn}")
                return
        print("Book not found or already available.")
