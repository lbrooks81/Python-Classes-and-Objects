from random import * 
from dnd import get_starting_stats
import os

class Monster:
    name : str
    hp : int
    strength : int
    defense : int
    speed : int

    def __init__(self, name) -> None:
        self.name = name
        self.hp = 40
        self.strength = get_starting_stats()
        self.defense = 1
        self.speed = get_starting_stats()

    def take_damage(self, initial_damage : int, monster_defense : int) -> None:
        if initial_damage < 0:
            return
        critical_multiplier = 2 if randint(1, 10) == 10 else 1
        
        damage_received = (initial_damage - monster_defense) * critical_multiplier
        self.hp -= damage_received
        print(f"{self.name} took {damage_received} damage. Remaining HP: {self.hp}\n")

    def is_Kod(self) -> bool:
        return True if self.hp <= 0 else False
    
class Arena:
    monster1 : Monster
    monster2 : Monster

    def __init__(self, monster1, monster2) -> None:
        self.monster1 = monster1
        self.monster2 = monster2
    
    def fight(self) -> None:

        print(f"{self.monster1.name} vs {self.monster2.name}")
        
        max(self.monster1.speed, self.monster2.speed)
        turn_counter : int = 1

        while(True):
            print(f"=====Turn {turn_counter}=====")
            monster_turn = self.determine_turn_order()

            monster_turn[0].take_damage(monster_turn[1].strength, monster_turn[0].defense)
            if monster_turn[0].is_Kod():
                break
            monster_turn[1].take_damage(monster_turn[0].strength, monster_turn[1].defense)
            if monster_turn[1].is_Kod():
                break
            turn_counter += 1

        print(f"{self.fight_winner().name} won the fight!")
        
    def determine_turn_order (self) -> list:
        """Returns the turn order of the monsters based on speed stats"""
        # Monster 1 goes first
        if self.monster1.speed > self.monster2.speed:
            return [self.monster1, self.monster2]
        
        # Randomly chooses a monster if both monsters have the same speed
        if self.monster1.speed == self.monster2.speed:
            first_turn = choice((self.monster1, self.monster2))
            second_turn = self.monster1 if first_turn == self.monster2 else self.monster2
            return [first_turn, second_turn]
        
        # Monster 2 goes first
        return [self.monster2, self.monster1]

    def fight_winner(self):
        """Returns the monster that won the fight"""
        if self.monster1.is_Kod():
            return self.monster2
        else:
            return self.monster1

os.system('cls')

pumbio = Monster('Pumbio')
splungis = Monster('Splungis')

dumber_dome = Arena(pumbio, splungis)
dumber_dome.fight()

