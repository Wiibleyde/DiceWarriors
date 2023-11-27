from serializable import Serializable
from classe import Ogre, Golem, Phantom, Zombie, Skeleton
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

random_skeleton_names = [
    "Bone bag",
    "Bone alloy"
]

class Progression(Serializable):
    def __init__(self, _level: int) -> None:
        self._level = _level

    def get_character_name(self):
        return self._character_name
    
    def get_level(self):
        return self._level
    
    def get_level_mobs(self):
        level_mobs = []
        if self._level == 1:
            zombie1 = Zombie(random.choice(random_zombie_names), 7, 3, 0, Dice(12))
            squelette1 = Skeleton(random.choice(random_skeleton_names), 7, 3, 0, Dice(12))
            level_mobs.append(zombie1)
            level_mobs.append(squelette1)
        elif self._level == 2:
            ogre1 = Ogre(random.choice(random_ogre_names), 10, 5, 1, Dice(9))
            ogre2 = Ogre(random.choice(random_ogre_names), 10, 5, 1, Dice(9))
            level_mobs.append(ogre1)
            level_mobs.append(ogre2)
        elif self._level == 3:
            golem1 = Golem(random.choice(random_golem_names), 15, 7, 1, Dice(8))
            golem2 = Golem(random.choice(random_golem_names), 15, 7, 1, Dice(8))
            level_mobs.append(golem1)
            level_mobs.append(golem2)
        elif self._level == 4:
            phantom1 = Phantom(random.choice(random_phantom_names), 15, 10, 0, Dice(5))
            phantom2 = Phantom(random.choice(random_phantom_names), 15, 10, 0, Dice(5))
            level_mobs.append(phantom1)
            level_mobs.append(phantom2)
        elif self._level == 5:
            zombie1 = Zombie(random.choice(random_zombie_names), 5, 3, 2, Dice(3))
            ogre1 = Ogre(random.choice(random_ogre_names), 10, 5, 3, Dice(5))
            golem1 = Golem(random.choice(random_golem_names), 15, 7, 4, Dice(6))
            phantom1 = Phantom(random.choice(random_phantom_names), 20, 10, 3, Dice(6))
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