import random

from character import Warrior, Mage, Thief
from dice import Dice

def main():
    warrior = Warrior(_name="Nathan", _dice=Dice(6), _attack_value=8, _defense_value=3, _max_health=20)
    mage = Mage(_name="Eva", _dice=Dice(6), _attack_value=8, _defense_value=3, _max_health=20)
    thief = Thief(_name="Samuel", _dice=Dice(6), _attack_value=8, _defense_value=3, _max_health=20)

    characters = [warrior, mage, thief]
    stats = {}

    car1 = random.choice(characters)
    characters.remove(car1)

    car2 = random.choice(characters)
    characters.remove(car2)

    stats[car1.get_name()] = 0
    stats[car2.get_name()] = 0

    for compteur in range(100):
        print(f"Combat {compteur + 1}")
        car1.regenerate()
        car2.regenerate()
        while car1.is_alive() and car2.is_alive():
            car1.attack(car2)
            car2.attack(car1)
        if car1.is_alive():
            stats[car1.get_name()] += 1
        else:
            stats[car2.get_name()] += 1
    
    print(f"Stats: {stats}")

if __name__ == "__main__":
    main()