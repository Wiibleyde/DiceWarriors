import json

from character import Character, Warrior
from dice import Dice

class Save:
    def __init__(self, path: str = "save.json"):
        self.path = path
        self.data = []
        try:
            self.load()
        except FileNotFoundError:
            self.save()

    def load(self):
        with open(self.path, "r") as file:
            self.data = json.load(file)

    def save(self):
        with open(self.path, "w") as file:
            json.dump(self.data, file)

    def add(self, character: Character):
        if character.get_name() not in [character["_name"] for character in self.data]:
            self.data.append(character.to_dict())
            self.save()
            return True
        return False
    
    def update(self, character: Character):
        for index, character_data in enumerate(self.data):
            if character_data["_name"] == character.get_name():
                self.data[index] = character.to_dict()
                self.save()
                return True
        return False

    def remove(self, name: str):
        for character in self.data:
            if character["_name"] == name:
                self.data.remove(character)
                self.save()
                return True
        return False

    def get(self, name: str):
        for character in self.data:
            if character["_name"] == name:
                return Character.from_dict(character)
        return None
    
    def get_all(self):
        return [Character.from_dict(character) for character in self.data]
    
if __name__=='__main__':
    save = Save()
    char = Warrior("Alice", 100, 10, 10, Dice(6), 0)
    print(char)
    save.add(char)
    print(save.get_all())
    for character in save.get_all():
        print(character)
        print(character._max_health)
        print(character._current_health)
        print(character._dice.roll())
    # save.remove("Alice")
