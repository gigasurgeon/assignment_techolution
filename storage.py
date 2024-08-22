import json
import os

class Storage:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_data(self):
        #if the json file doesn't exist, return an empty list
        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except Exception as e:
            return []

    def save_data(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)
