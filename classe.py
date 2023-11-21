from character import Character

# Personnage
class Paladin(Character):
    def compute_damages(self, roll, target):
        print("Bonus : (+3 attack)")
        return super().compute_damages(roll, target) +3
        
class Warlock(Character):
    def compute_defense(self, damages , roll, attacker):
        print("Bonus : (+3 defense)")
        return super().compute_defense(damages, roll, attacker) -3

class Assassin(Character):
    def compute_damages(self, roll, target: Character):
        print (f"Bonus : (ignore defene + {target.get_defense_value()})")
        return super().compute_damages(roll, target) + target.get_defense_value()

class Executor(Character):
    def attack(self, target: Character):
        super().attack(target)

        if target.is_alive() and target._current_health <= 5:
            print(f"{target.get_name()} est en danger critique et est éliminé automatiquement !")
            target._current_health = 0
            target.show_healthbar()

class MarksMan(Character):
    pass

# Monstre
class Phantom(Character):
    def defense(self, damages, attacker):
        roll = self._dice.roll()
        if roll <= 2:
            print(f"{self._name} évite l'attaque de {attacker.get_name()} avec agilité !")
        else:
            super().compute_defense(damages, roll, attacker)

class Ogre(Character):
    pass

class Skeleton(Character):
    pass

class Zombie(Character):
    def compute_defense(self, damages, roll, attacker):
        print("---")
        print(f"{self._name} a maintenant {self._current_health}")
        print("---")
        return super().compute_defense(damages, roll, attacker)

class Golem(Character):
    pass

