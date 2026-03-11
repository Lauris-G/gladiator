#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## fight.py
##

class Warrior:
    def __init__ (self, hp, strenght, defense, initiative):
        self.hp = hp
        self.max_hp = hp
        self.strenght = strenght
        self.defense = defense
        self.initiative = initiative