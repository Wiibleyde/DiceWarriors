from __future__ import annotations
from dice import Dice

from rich import print

class Character:
    
    def __init__(self, name: str, max_health: int, attack: int, defense: int, dice) -> None:
        self._name = name
        self._max_health = max_health
        self._current_health = max_health
        self._attack_value = attack
        self._defense_value = defense
        self._dice = dice
        
    def __str__(self):
        return f"I'm {self._name} the Character with attack: {self._attack_value} and defense: {self._defense_value}"
    
    def get_name(self):
        return self._name
    
    def get_defense_value(self):
        return self._defense_value
    
    def get_current_health(self):
        return self._current_health
    
    def get_max_health(self):
        return self._max_health
    
    def get_attack_value(self):
        return self._attack_value
    
    def get_defense_value(self):
        return self._defense_value
    
    def to_dict(self):
        return {
            "name": self._name,
            "max_health": self._max_health,
            "current_health": self._current_health,
            "attack_value": self._attack_value,
            "defense_value": self._defense_value,
            "dice": self._dice._sides
        }
    
    def is_alive(self):
        # return bool(self._current_health)
        return self._current_health > 0
        
    def decrease_health(self, amount: int):
        if (self._current_health - amount) < 0:
            amount = self._current_health
        self._current_health -= amount
        self.show_healthbar()
        
    def show_healthbar(self):
        if not self.is_alive():
            return
        missing_hp = self._max_health - self._current_health
        healthbar = f"[{'⬜' * self._current_health}{'☐' * missing_hp}] {self._current_health}/{self._max_health}hp"
        print(healthbar)

    def regenerate(self):
        self._current_health = self._max_health

    def compute_damages(self, roll: int, target: Character):
        return self._attack_value + roll

    def compute_defense(self, damages: int, roll: int, attacker: Character):
        return damages - self._defense_value - roll

    def attack(self, target: Character):
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages} damages in your face ! (attack: {self._attack_value} + roll: {damages - self._attack_value})")
        target.defense(damages, self)
    
    def defense(self, damages: int, attacker: Character):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll, attacker)
        print(f"🛡️ {self._name} take {wounds} wounds from {attacker.get_name()} in his face ! (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)

class Warrior(Character):
    def compute_damages(self, roll: int, target: Character):
        print(f"🪓 Bonus: Axe in your face ! (+3 damages)")
        return super().compute_damages(roll, target) + 3

class Mage(Character):
    def compute_defense(self, damages: int, roll: int, attacker: Character):
        print(f"🧙 Bonus: Magic protection ! (-3 wounds)")
        return super().compute_defense(damages, roll, attacker) - 3

class Thief(Character):
    def compute_damages(self, roll: int, target: Character):
        print(f"🔪 Bonus: Ignore defense")
        return super().compute_damages(roll, target) + target.get_defense_value()

if __name__ == "__main__":
    a_dice = Dice(6)

    character1 = Thief("Gerard", 20, 8, 3, Dice(6))
    character2 = Warrior("Lisa", 20, 8, 3, Dice(6))
    #print(character1)
    #print(character2)
    
    while(character1.is_alive() and character2.is_alive()):
        character1.attack(character2)
        character2.attack(character1)