#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## object.py
##

import math

FRENCH_NAMES = {
    "sword": "Épée",
    "spear": "Lance",
    "net": "Filet"
}

class OBJECT:
    BASE_MULTIPLIER = 1.5

    def __init__(self, name, attack=0, defense=0, price=0):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.base_price = price
        self.price = price
        self.owned = False
        self.level = 0
        self.message = ""

    def get_french_name(self):
        return FRENCH_NAMES.get(self.name, self.name)

    def equip(self, buyer):
        french_name = self.get_french_name()
        if not self.owned:
            self.message = f"{french_name} n'est pas encore acheté."
            return False
        buyer.weapon = self.name
        self.message = f"{french_name} équipée."
        return True

    def upgrade_price(self):
        return math.floor(self.base_price * (self.BASE_MULTIPLIER ** self.level))

    def buy(self, buyer):
        french_name = self.get_french_name()
        if self.owned:
            self.message = f"{french_name} est déjà acheté."
            return False
        if self.price > buyer.gold:
            self.message = f"Pas assez d'or. (nécessaire: {self.price}, disponible: {buyer.gold})"
            return False
        else:
            buyer.gold -= self.price
            self.owned = True
            buyer.inventory.append(self)
            self.message = f"{french_name} acheté pour {self.price} pièces."
            return True
    
    def upgrade(self, buyer):
        french_name = self.get_french_name()
        if not self.owned:
            self.message = f"{french_name} n'est pas encore acheté."
            return False
        cost = self.upgrade_price()
        if cost > buyer.gold:
            self.message = f"Pas assez d'or pour améliorer. (nécessaire: {cost}, disponible: {buyer.gold})"
            return False
        buyer.gold -= cost
        self.level += 1
        self.attack = round(self.attack * 1.2)
        self.defense = round(self.defense * 1.2)
        print(f"{french_name} amélioré au niveau {self.level} pour {cost} pièces.")
        return True
        
    def __repr__(self):
        return (f"{self.name} | Niv.{self.level} | "
                f"ATK:{self.attack} DEF:{self.defense} | "
                f"{'[Possédé]' if self.owned else f'Prix:{self.price}'}")