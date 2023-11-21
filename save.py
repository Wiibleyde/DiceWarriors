import json

from character import Character

class Save:
    def __init__(self, path: str = "save.json"):
        self.path = path
        self.data = []
        self.load()

    def load(self):
        with open(self.path, "r") as file:
            self.data = json.load(file)

    def save(self):
        with open(self.path, "w") as file:
            json.dump(self.data, file)

    def add(self, character: Character):
        self.data.append(json.dumps(character.__dict__))
        self.save()

    def remove(self, name: str):
        for character in self.data:
            if character["name"] == name:
                self.data.remove(character)
                self.save()
                return True
        return False

    def get(self, name: str):
        for character in self.data:
            if character["name"] == name:
                return Character.from_dict(character)
        return None
    
    def get_all(self):
        print(self.data)
        return [Character.from_dict(character) for character in self.data]