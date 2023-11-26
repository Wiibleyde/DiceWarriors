from character import Character

# Personnage
class Paladin(Character):
    def compute_damages(self, roll, target):
        #print("\n")
        print("Bonus : (+3 attack)")
        return super().compute_damages(roll, target) +3
        
class Warlock(Character):
    def compute_defense(self, damages , roll, attacker):
        #print("\n")
        print("Bonus : (+3 defense)")
        return super().compute_defense(damages, roll, attacker) -3

class Assassin(Character):
    def compute_damages(self, roll, target: Character):
        #print("\n")
        print (f"Bonus : (ignore defene + {target.get_defense_value()})")
        return super().compute_damages(roll, target) + target.get_defense_value()

class Executor(Character):
    def attack(self, target: Character):
        super().attack(target)

        if target.is_alive() and target._current_health <= 5:
            #print("\n")
            print(f"{target.get_name()} est en danger critique et est éliminé automatiquement !")
            target._current_health = 0

class MarksMan(Character):
    pass

# Monstre
class Ogre(Character):
    def compute_damages(self, roll, target):
        #print("\n")
        print("Bonus : (+3 attack)")
        return super().compute_damages(roll, target) +3

class Golem(Character):
    def compute_defense(self, damages , roll, attacker):
        #print("\n")
        print("Bonus : (+3 defense)")
        return super().compute_defense(damages, roll, attacker) -3

class Phantom(Character):
    def defense(self, damages, attacker):
        roll = self._dice.roll()
        if roll <= 2:
            #print("\n")
            print(f"{self._name} évite l'attaque de {attacker.get_name()} avec agilité !")
        else:
            super().compute_defense(damages, roll, attacker)

class Zombie(Character):
    def decrease_health(self, amount):
        print(f"🩸 {self._name} take {amount} damages in his face !")
        if not self._current_health - amount <= 0:
            if self._current_health <= 5:
                regenerated_health = 5
                print(f"{self._name} se régénère et a maintenant {regenerated_health} HP !")
                self._current_health = regenerated_health
            else:
                print(f"{self._name} a maintenant {self._current_health - amount} HP !")
                amount = self._current_health
        else:
            super().decrease_health(amount)

    def regenerate(self):
        self._current_health = self._max_health

class Skeleton(Character):
    pass