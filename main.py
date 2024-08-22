from book_management import BookManager
from user_management import UserManager
from checkout_management import CheckoutManager
from logs import log_activity

def main_menu():
    # Display the main menu and get the user's choice
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search Books")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Add User")
    print("7. List Users")
    print("8. Search Users")
    print("9. Update User")
    print("10. Delete User")
    print("11. Checkout Book")
    print("12. Check-in Book")
    print("13. Exit")
    return input("Enter choice: ")

def main():
    #initialize objects
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager()

    while True:
        #get the user input
        choice = main_menu()

        #perform actions based on user's input
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
            log_activity(f"Book added: {title}, {author}, {isbn}")
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            title = input("Enter title to search (leave blank if not applicable): ")
            author = input("Enter author to search (leave blank if not applicable): ")
            isbn = input("Enter ISBN to search (leave blank if not applicable): ")
            book_manager.search_books(title, author, isbn)
        elif choice == '4':
            isbn = input("Enter ISBN of the book to update: ")
            new_title = input("Enter new title (leave blank if not applicable): ")
            new_author = input("Enter new author (leave blank if not applicable): ")
            book_manager.update_book(isbn, new_title, new_author)
            log_activity(f"Book updated: {isbn}")
        elif choice == '5':
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)
            log_activity(f"Book deleted: {isbn}")
        elif choice == '6':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
            log_activity(f"User added: {name}, {user_id}")
        elif choice == '7':
            user_manager.list_users()
        elif choice == '8':
            name = input("Enter name to search (leave blank if not applicable): ")
            user_id = input("Enter User ID to search (leave blank if not applicable): ")
            user_manager.search_users(name, user_id)
        elif choice == '9':
            user_id = input("Enter User ID of the user to update: ")
            new_name = input("Enter new name (leave blank if not applicable): ")
            user_manager.update_user(user_id, new_name)
            log_activity(f"User updated: {user_id}")
        elif choice == '10':
            user_id = input("Enter User ID of the user to delete: ")
            user_manager.delete_user(user_id)
            log_activity(f"User deleted: {user_id}")
        elif choice == '11':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            checkout_manager.checkout_book(user_id, isbn)
            log_activity(f"Book checked out: {isbn} by User {user_id}")
        elif choice == '12':
            isbn = input("Enter ISBN of the book to check-in: ")
            checkout_manager.checkin_book(isbn)
            log_activity(f"Book checked in: {isbn}")
        elif choice == '13':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
