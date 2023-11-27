from character import Character

# Personnage
class Paladin(Character):
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) +3
        
class Warlock(Character):
    def compute_defense(self, damages , roll, attacker):
        return super().compute_defense(damages, roll, attacker) -3

class Assassin(Character):
    def compute_damages(self, roll, target: Character):
        return super().compute_damages(roll, target) + target.get_defense_value()

class Executor(Character):
    def attack(self, target: Character):
        super().attack(target)

        if target.is_alive() and target._current_health <= 5:
            target._current_health = 0

class MarksMan(Character):
    pass

# Monstre
class Ogre(Character):
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) +3

class Golem(Character):
    def compute_defense(self, damages , roll, attacker):
        return super().compute_defense(damages, roll, attacker) -3

class Phantom(Character):
    def defense(self, damages, attacker):
        roll = self._dice.roll()
        if roll <= 1:
            print(f"{self._name} esquive l'attaque !")
        else:
            wounds = super().compute_defense(damages, roll, attacker)
            self.decrease_health(wounds)

class Zombie(Character):
    def decrease_health(self, amount):
        if not self._current_health - amount <= 0:
            if self._current_health <= 5:
                regenerated_health = 5
                self._current_health = regenerated_health
            else:
                amount = self._current_health
        else:
            super().decrease_health(amount)

    def regenerate(self):
        self._current_health = self._max_health

class Skeleton(Character):
    pass