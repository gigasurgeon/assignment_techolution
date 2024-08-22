from models import User
from storage import Storage

class UserManager:
    def __init__(self):
        self.storage = Storage('users.json')
        self.users = self.storage.load_data()

    def add_user(self, name, user_id):
        #prevent adding a duplicate user
        if any(user['user_id'] == user_id for user in self.users):
            print("User with this ID already exists.")
            return
        new_user = User(name, user_id)
        self.users.append(new_user.__dict__)
        self.storage.save_data(self.users)
        print(f"Added: {new_user.name}")

    def update_user(self, user_id, new_name=None):
        #update the user's name if they exist
        for user in self.users:
            if user['user_id'] == user_id:
                if new_name:
                    user['name'] = new_name
                self.storage.save_data(self.users)
                print(f"Updated user with ID: {user_id}")
                return
        print("User not found.")

    def delete_user(self, user_id):
        #remove the user if they exist
        original_count = len(self.users)
        self.users = [user for user in self.users if user['user_id'] != user_id]
        if len(self.users) < original_count:
            self.storage.save_data(self.users)
            print(f"Deleted user with ID: {user_id}")
        else:
            print("User not found.")

    def list_users(self):
        #print all users in the system
        for user in self.users:
            print(User(**user))

    def search_users(self, name=None, user_id=None):
        #find the relevant users
        results = [
            user for user in self.users
            if (name and name.lower() in user['name'].lower()) or
               (user_id and user['user_id'] == user_id)
        ]
        if results:
            for user in results:
                print(User(**user))
        else:
            print("No matching users found.")
