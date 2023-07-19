import json

class Data:

    def __init__(self, path):
        self.path = path

    def save_to_json(self, data=[]):
        try:
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
        except FileNotFoundError as e:
            print(e)

    def load_from_json(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except FileNotFoundError as e:
            self.save_to_json()

