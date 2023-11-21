from random import randint

from serializable import Serializable

class Dice(Serializable):
    def __init__(self, sides: int = 6):
        self._sides = sides

    def __str__(self) -> str:
        return f"{self._sides}-sided dice"
    
    def __getattribute__(self, __name: str) -> int:
        return super().__getattribute__(__name)

    def roll(self) -> int:
        return randint(1, self._sides)
    
    def to_dict(self) -> dict:
        return {
            "sides": self._sides
        }
    
class RiggedDice(Dice, Serializable):
    def __init__(self, sides: int = 6, rigged_value: int = 6):
        super().__init__(sides)
        self._rigged_value = rigged_value

    def __str__(self) -> str:
        return f"{self._sides}-sided dice rigged to {self._rigged_value}"

    def roll(self, rigged: bool = False) -> int:
        return super().roll() if not rigged else self._rigged_value
    
    def to_dict(self) -> dict:
        return {
            "sides": self._sides,
            "rigged_value": self._rigged_value
        }

if __name__=='__main__':
    riggedDice = RiggedDice(sides=20, rigged_value=20)
    print(riggedDice.roll(True))