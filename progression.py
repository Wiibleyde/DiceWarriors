from serializable import Serializable
from classe import Ogre, Golem, Phantom, Zombie
from dice import Dice
import random

random_zombie_names = [
    "Dead thing but in fact no",
    "The Walking Not Alive",
    "Green thing"
]

random_ogre_names = [
    "Shreek",
    "Ugly big thing",
    "Big green thing"
]

random_golem_names = [
    "Iron Golem",
    "Statue",
    "Rocky (but not the OS)"
]

random_phantom_names = [
    "Flying sheet",
    "Scary thing",
    "Boooooo"
]

class Progression(Serializable):
    def __init__(self, _level: int) -> None:
        self._level = _level

    def get_character_name(self):
        return self._character_name
    
    def get_level(self):
        return self._level
    
    def get_level_mobs(self):
        print(self._level)
        level_mobs = []
        if self._level == 1:
            print("Level 1")
            zombie1 = Zombie(random.choice(random_zombie_names), 5, 3, 2, Dice(3))
            zombie2 = Zombie(random.choice(random_zombie_names), 5, 3, 2, Dice(3))
            level_mobs.append(zombie1)
            level_mobs.append(zombie2)
        elif self._level == 2:
            print("Level 2")
            ogre1 = Ogre(random.choice(random_ogre_names), 10, 5, 3, Dice(6))
            ogre2 = Ogre(random.choice(random_ogre_names), 10, 5, 3, Dice(6))
            level_mobs.append(ogre1)
            level_mobs.append(ogre2)
        elif self._level == 3:
            print("Level 3")
            golem1 = Golem(random.choice(random_golem_names), 15, 7, 4, Dice(9))
            golem2 = Golem(random.choice(random_golem_names), 15, 7, 4, Dice(9))
            level_mobs.append(golem1)
            level_mobs.append(golem2)
        elif self._level == 4:
            print("Level 4")
            phantom1 = Phantom(random.choice(random_phantom_names), 20, 10, 5, Dice(12))
            phantom2 = Phantom(random.choice(random_phantom_names), 20, 10, 5, Dice(12))
            level_mobs.append(phantom1)
            level_mobs.append(phantom2)
        elif self._level == 5:
            print("Level 5")
            zombie1 = Zombie(random.choice(random_zombie_names), 5, 3, 2, Dice(3))
            ogre1 = Ogre(random.choice(random_ogre_names), 10, 5, 3, Dice(6))
            golem1 = Golem(random.choice(random_golem_names), 15, 7, 4, Dice(9))
            phantom1 = Phantom(random.choice(random_phantom_names), 20, 10, 5, Dice(12))
            level_mobs.append(zombie1)
            level_mobs.append(ogre1)
            level_mobs.append(golem1)
            level_mobs.append(phantom1)
        else:
            print("Level not found")
        return level_mobs

if __name__=="__main__":
    progression = Progression(1)
    print(progression.get_level_mobs())