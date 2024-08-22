import unittest
from unittest.mock import patch, MagicMock
from book_management import BookManager
from user_management import UserManager
from checkout_management import CheckoutManager


class TestBookManager(unittest.TestCase):
    @patch('book_management.Book')
    @patch('book_management.Storage')
    def test_add_book(self, MockStorage, MockBook):
        mock_storage = MockStorage.return_value
        mock_storage.load_data.return_value = []
        MockBook.return_value.__dict__ = {"title": "Title", "author": "Author", "isbn": "12345", "available": True}

        book_manager = BookManager()
        book_manager.add_book("Title", "Author", "12345")
        mock_storage.save_data.assert_called_with([{"title": "Title", "author": "Author", "isbn": "12345", "available": True}])

    @patch('book_management.Storage')
    def test_update_book(self, MockStorage):
        mock_storage = MockStorage.return_value
        mock_storage.load_data.return_value = [{"title": "Old Title", "author": "Old Author", "isbn": "12345", "available": True}]

        book_manager = BookManager()
        book_manager.update_book("12345", new_title="New Title", new_author="New Author")

        mock_storage.save_data.assert_called_with([{"title": "New Title", "author": "New Author", "isbn": "12345", "available": True}])

    @patch('book_management.Storage')
    def test_delete_book(self, MockStorage):
        mock_storage = MockStorage.return_value
        mock_storage.load_data.return_value = [{"title": "Title", "author": "Author", "isbn": "12345", "available": True}]

        book_manager = BookManager()
        book_manager.delete_book("12345")

        mock_storage.save_data.assert_called_with([])


class TestUserManager(unittest.TestCase):
    @patch('user_management.User')
    @patch('user_management.Storage')
    def test_add_user(self, MockStorage, MockUser):
        mock_storage = MockStorage.return_value
        mock_storage.load_data.return_value = []
        MockUser.return_value.__dict__ = {"name": "Name", "user_id": "user1"}

        user_manager = UserManager()
        user_manager.add_user("Name", "user1")
        mock_storage.save_data.assert_called_with([{"name": "Name", "user_id": "user1"}])

    @patch('user_management.Storage')
    def test_update_user(self, MockStorage):
        mock_storage = MockStorage.return_value
        mock_storage.load_data.return_value = [{"name": "Old Name", "user_id": "user1"}]

        user_manager = UserManager()
        user_manager.update_user("user1", new_name="New Name")

        mock_storage.save_data.assert_called_with([{"name": "New Name", "user_id": "user1"}])

    @patch('user_management.Storage')
    def test_delete_user(self, MockStorage):
        mock_storage = MockStorage.return_value
        mock_storage.load_data.return_value = [{"name": "Name", "user_id": "user1"}]

        user_manager = UserManager()
        user_manager.delete_user("user1")

        mock_storage.save_data.assert_called_with([])


class TestCheckoutManager(unittest.TestCase):
    def setUp(self):
        self.manager = CheckoutManager()
        self.manager.book_storage = MagicMock()
        self.manager.checkout_storage = MagicMock()
        self.manager.books = [{'title': 'Title', 'author': 'Author', 'isbn': '12345', 'available': True}]
        self.manager.checkouts = []

    def test_checkout_book(self):
        self.manager.checkout_book('user1', '12345')
        self.assertEqual(len(self.manager.checkouts), 1)
        self.assertFalse(self.manager.books[0]['available'])

    def test_checkin_book(self):
        self.manager.books[0]['available'] = False
        self.manager.checkouts = [{'user_id': 'user1', 'isbn': '12345'}]
        self.manager.checkin_book('12345')
        self.assertTrue(self.manager.books[0]['available'])
        self.assertEqual(len(self.manager.checkouts), 0)

if __name__ == '__main__':
    unittest.main()
