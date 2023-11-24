import tkinter as tk
from tkinter.messagebox import showinfo
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from character import *
from dice import Dice
from save import Save
from progression import Progression

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Warrior")
        self.root.geometry("800x600")
        self.root.minsize(800, 600)
        self.root.maxsize(800, 600)
        self.root.style = ttk.Style()
        self.root.style.theme_use("superhero")

        self.main_page()

        self.root.mainloop()


    def main_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = ttk.Label(self.root, text="Dice Warrior", font=("Arial", 40))
        self.label.pack(pady=10)

        self.text = ttk.Label(self.root, text="Welcome to Dice Warrior! This is a game where you fight enemies using dice rolls. Good luck!")
        self.text.pack(pady=10)

        self.button = ttk.Button(self.root, text="New Game", command=self.new_game_page)
        self.button.pack(pady=10)

        self.button = ttk.Button(self.root, text="Load Game", command=self.load_game_page)
        self.button.pack(pady=10)

        self.button = ttk.Button(self.root, text="Quit", command=self.root.quit)
        self.button.pack(pady=10)

    def new_game_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = ttk.Label(self.root, text="Dice Warrior", font=("Arial", 40))
        self.label.pack(pady=10)

        self.text = ttk.Label(self.root, text="Choose your character:")
        self.text.pack(pady=10)

        self.button = ttk.Button(self.root, text="Warrior", command=lambda: self.new_game("Warrior"))
        self.button.pack(pady=10)

        self.button = ttk.Button(self.root, text="Mage", command=lambda: self.new_game("Mage"))
        self.button.pack(pady=10)

        self.button = ttk.Button(self.root, text="Thief", command=lambda: self.new_game("Thief"))
        self.button.pack(pady=10)

        self.button = ttk.Button(self.root, text="Back", command=self.main_page)
        self.button.pack(pady=10)

    def new_game(self, character: str):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = ttk.Label(self.root, text="Dice Warrior", font=("Arial", 40))
        self.label.pack(pady=10)

        self.confirmed = False
        
        self.max_points = 5
        self.defaultAtk = 10
        self.defaultDef = 10
        self.defaultHealth = 10

        self.capTxt = ttk.Label(self.root, text=f"Capacity points: you have {self.max_points} points to spend")
        self.capTxt.pack(pady=10)

        self.nameTxt = ttk.Label(self.root, text=f"Name:")
        self.nameTxt.pack(pady=10)

        self.nameInput = ttk.Entry(self.root)
        self.nameInput.pack(pady=10)

        self.text = ttk.Label(self.root, text=f"Attack:")
        self.text.pack(pady=10)
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=10)
        self.button = ttk.Button(self.frame, text="-5", command=lambda: self.decrease_attack(5), style="danger.TButton")
        self.button.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.button = ttk.Button(self.frame, text="-", command=lambda: self.decrease_attack(1), style="danger.TButton")
        self.button.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.atkVal = ttk.Label(self.frame, text=f"{self.defaultAtk}")
        self.atkVal.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.button = ttk.Button(self.frame, text="+", command=lambda: self.increase_attack(1), style="success.TButton")
        self.button.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.button = ttk.Button(self.frame, text="+5", command=lambda: self.increase_attack(5), style="success.TButton")
        self.button.pack(side=tk.LEFT)
        

        self.text = ttk.Label(self.root, text=f"Defense:")
        self.text.pack(pady=10)
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=10)
        self.button = ttk.Button(self.frame, text="-5", command=lambda: self.decrease_defense(5), style="danger.TButton")
        self.button.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.button = ttk.Button(self.frame, text="-", command=lambda: self.decrease_defense(1), style="danger.TButton")
        self.button.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.defVal = ttk.Label(self.frame, text=f"{self.defaultDef}")
        self.defVal.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.button = ttk.Button(self.frame, text="+", command=lambda: self.increase_defense(1), style="success.TButton")
        self.button.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.button = ttk.Button(self.frame, text="+5", command=lambda: self.increase_defense(5), style="success.TButton")
        self.button.pack(side=tk.LEFT)

        self.text = ttk.Label(self.root, text=f"Health:")
        self.text.pack(pady=10)
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=10)
        self.button = ttk.Button(self.frame, text="-5", command=lambda: self.decrease_health(5), style="danger.TButton")
        self.button.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.button = ttk.Button(self.frame, text="-", command=lambda: self.decrease_health(1), style="danger.TButton")
        self.button.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.healthVal = ttk.Label(self.frame, text=f"{self.defaultHealth}")
        self.healthVal.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.button = ttk.Button(self.frame, text="+", command=lambda: self.increase_health(1), style="success.TButton")
        self.button.pack(side=tk.LEFT)
        self.empty = ttk.Label(self.frame, text=" ")
        self.empty.pack(side=tk.LEFT)
        self.button = ttk.Button(self.frame, text="+5", command=lambda: self.increase_health(5), style="success.TButton")
        self.button.pack(side=tk.LEFT)

        self.button = ttk.Button(self.root, text="Create", command=lambda: self.create_character(character))
        self.button.pack(pady=10)
        
        self.frame = ttk.Frame(self.root)

        self.button = ttk.Button(self.frame, text="Back", command=self.new_game_page)
        self.button.pack(side=tk.LEFT, pady=10)
        self.button = ttk.Button(self.frame, text="Quit", command=self.root.quit)
        self.button.pack(side=tk.LEFT, pady=10)
        self.frame.pack(pady=10)

    def increase_attack(self, value: int):
        points = int(self.capTxt["text"].split(" ")[-4])
        if points - value >= 0:
            self.atkVal["text"] = str(int(self.atkVal["text"]) + value)
            self.capTxt["text"] = f"Capacity points: you have {points - value} points to spend"

    def decrease_attack(self, value: int):
        points = int(self.capTxt["text"].split(" ")[-4])
        if points + value <= self.max_points:
            self.atkVal["text"] = str(int(self.atkVal["text"]) - value)
            self.capTxt["text"] = f"Capacity points: you have {points + value} points to spend"

    def increase_defense(self, value: int):
        points = int(self.capTxt["text"].split(" ")[-4])
        if points - value >= 0:
            self.defVal["text"] = str(int(self.defVal["text"]) + value)
            self.capTxt["text"] = f"Capacity points: you have {points - value} points to spend"

    def decrease_defense(self, value: int):
        points = int(self.capTxt["text"].split(" ")[-4])
        if points + value <= self.max_points:
            self.defVal["text"] = str(int(self.defVal["text"]) - value)
            self.capTxt["text"] = f"Capacity points: you have {points + value} points to spend"

    def increase_health(self, value: int):
        points = int(self.capTxt["text"].split(" ")[-4])
        if points - value >= 0:
            self.healthVal["text"] = str(int(self.healthVal["text"]) + value)
            self.capTxt["text"] = f"Capacity points: you have {points - value} points to spend"

    def decrease_health(self, value: int):
        points = int(self.capTxt["text"].split(" ")[-4])
        if points + value <= self.max_points:
            self.healthVal["text"] = str(int(self.healthVal["text"]) - value)
            self.capTxt["text"] = f"Capacity points: you have {points + value} points to spend"

    def create_character(self, character: str):
        name = self.nameInput.get()
        if name == "":
            # Add a popup
            showinfo("Error", "You must enter a name")
            return
        
        pointsLeft = int(self.capTxt["text"].split(" ")[-4])
        if pointsLeft != 0 and not self.confirmed:
            showinfo("Warning", "You have points left to spend")
            self.confirmed = True
            return
        attack = int(self.atkVal["text"])
        defense = int(self.defVal["text"])
        health = int(self.healthVal["text"])

        if character == "Warrior":
            self.player = Warrior(name, health, attack, defense, Dice(6))
        elif character == "Mage":
            self.player = Mage(name, health, attack, defense, Dice(6))
        elif character == "Thief":
            self.player = Thief(name, health, attack, defense, Dice(6))
        resp = Save().add(self.player)
        if not resp:
            showinfo("Error", "A character with this name already exsits, chose another one.")
            return
        self.enemies = Progression(1).get_level_mobs()
        self.battle_page()

    def load_game_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = ttk.Label(self.root, text="Dice Warrior", font=("Arial", 40))
        self.label.pack(pady=10)

        self.text = ttk.Label(self.root, text="Choose your character:")
        self.text.pack(pady=10)

        self.characters = Save().get_all()
        self.buttons = []
        for character in self.characters:
            self.button = ttk.Button(self.root, text=character.get_name(), command=lambda character=character: self.load_game(character))
            self.button.pack(pady=10)
            self.buttons.append(self.button)

        self.button = ttk.Button(self.root, text="Back", command=self.main_page)
        self.button.pack(pady=10)

    def load_game(self, character: Character):
        self.player = character
        self.enemies = Progression(1).get_level_mobs()
        print(self.enemies)
        self.battle_page()

    def battle_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = ttk.Label(self.root, text="Dice Warrior", font=("Arial", 40))
        self.label.pack(pady=10)

        self.text = ttk.Label(self.root, text=f"{self.player.get_name()} vs {self.enemies[0].get_name()}")
        self.text.pack(pady=10)

        self.text = ttk.Label(self.root, text=f"{self.player.get_name()}: {self.player.get_current_health()}/{self.player.get_max_health()}hp")
        self.text.pack(pady=10)

        for enemy in self.enemies:
            self.text = ttk.Label(self.root, text=f"{enemy.get_name()}: {enemy.get_current_health()}/{enemy.get_max_health()}hp")
            self.text.pack(pady=10)

            self.button = ttk.Button(self.root, text="Attack", command=lambda: self.player.attack(enemy))
            self.button.pack(pady=10)

        self.button = ttk.Button(self.root, text="Save", command=self.save_game)
        self.button.pack(pady=10)

        self.button = ttk.Button(self.root, text="Quit", command=self.root.quit)
        self.button.pack(pady=10)
    
    def win(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = ttk.Label(self.root, text="Dice Warrior", font=("Arial", 40))
        self.label.pack(pady=10)

        self.text = ttk.Label(self.root, text=f"{self.player.get_name()} won!")
        self.text.pack(pady=10)

        self.button = ttk.Button(self.root, text="Continue", command=self.next_level)
        self.button.pack(pady=10)

        self.button = ttk.Button(self.root, text="Quit", command=self.root.quit)
        self.button.pack(pady=10)

    def lose(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = ttk.Label(self.root, text="Dice Warrior", font=("Arial", 40))
        self.label.pack(pady=10)

        self.text = ttk.Label(self.root, text=f"{self.player.get_name()} lost!")
        self.text.pack(pady=10)

        self.button = ttk.Button(self.root, text="Quit", command=self.root.quit)
        self.button.pack(pady=10)

    def next_level(self):
        self.player.increase_progression()
        self.enemies = Progression(self.player.get_progression()).get_level_mobs()
        self.battle_page()

    def save_game(self):
        Save().update(self.player)
        self.battle_page()
    
if __name__=='__main__':
    root = tk.Tk()
    Interface(root)