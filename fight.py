#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## fight.py
##

import random

def formate(n):
    return f"{n:_}".replace("_", " ")

class PLAYER:
    def __init__(self, name="", weapon="sword"):
        self.name = name
        self.maxhp = 100
        self.hp = self.maxhp
        self.attack = 10
        self.defense = 5
        self.weapon = weapon
        self.blocking = False
        self.gold = 0
        self.inventory = []
        self.equipped_armor = []

    def full_heal(self):
        self.hp = self.maxhp

    def add_gold(self, nb):
        self.gold += nb

class ENEMY:
    def __init__(self, name, weapon="sword", equipped_armor=None):
        self.name = name
        self.maxhp = 100
        self.hp = self.maxhp
        self.attack = 10
        self.defense = 5
        self.blocking = False
        self.weapon = weapon
        self.equipped_armor = equipped_armor if equipped_armor else []
    
    def full_heal(self):
        self.hp = self.maxhp

class FIGHT:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn = "player"
        self.message = ""
        self.turn_count = 1

    def simple_attack(self):
        if random.randint(1,100) < 90:
            damage = self.player.attack
            self.deal_damage(self.enemy, damage)
            self.message = f"{self.player.name} attaque : {formate(damage)} dégâts"
        else:
            self.message = f"{self.player.name} a raté !"
        self.end_turn()

    def heavy_attack(self):
        if random.randint(1,100) < 20:
            damage = self.player.attack * 2
            self.deal_damage(self.enemy, damage)
            self.message = f"{self.player.name} attaque puissante : {formate(damage)} dégâts"
        else:
            self.message = f"{self.player.name} a raté !"
        self.end_turn()

    def special_attack(self):
        weapon = self.player.weapon

        if (random.randint(1,100) < 70):
            if weapon == "sword":
                damage = self.player.attack
                if (random.randint(1, 100) < 30):
                    damage += self.player.attack // 2
                    self.message = f"{self.player.name} coup tranchant (saignement): {formate(damage)} dégâts"
                else:
                    self.message = f"{self.player.name} coup tranchant: {formate(damage)} dégâts"
                self.deal_damage(self.enemy, damage)
            
            elif weapon == "spear":
                damage = self.player.attack + 3
                self.deal_damage(self.enemy, damage)
                self.message = f"{self.player.name} estoc précise: {formate(damage)} dégâts"

            elif weapon == "net":
                self.enemy.blocking = True
                self.message = "Filet : ennemi immobilisé"

            else:
                damage = self.player.attack
                self.deal_damage(self.enemy, damage)
                self.message = f"{self.player.name} attaque spéciale: {formate(damage)} dégâts"
        else:
            self.message = f"{self.player.name} a raté !"
        self.end_turn()

    def block(self):
        self.player.blocking = True
        self.message = f"{self.player.name} se prépare à bloquer"
        self.end_turn()

    def enemy_turn(self):
        if not self.enemy.is_alive():
            return

        choice = random.choice(["attack", "heavy", "attack"])

        if choice == "attack":
            if random.randint(1,100) < 90:
                damage = self.enemy.attack
                self.deal_damage(self.player, damage)
                self.message += f"\n{self.enemy.name} attaque : {formate(damage)} dégâts"
            else:
                self.message += f"\n{self.enemy.name} a raté !"
        else:
            if random.randint(1,100) < 20:
                damage = self.enemy.attack * 2
                self.deal_damage(self.player, damage)
                self.message += f"\n{self.enemy.name} attaque puissante : {formate(damage)} dégâts"
            else:
                self.message += f"\n{self.enemy.name} a raté !"

        self.turn_count += 1
        self.turn = "player"

    def deal_damage(self, target, damage):

        if target.blocking:
            damage = damage // 2
            target.blocking = False

        damage = max(0, damage - target.defense)
        target.hp -= damage

    def end_turn(self):
        self.turn = "enemy"
        self.enemy_turn()

    def is_over(self):
        if self.player.hp <= 0:
            self.message = ""
            self.player.hp = 0
            return True
        if self.enemy.hp <= 0:
            self.message = ""
            self.enemy.hp = 0
            return True
        return False

def is_alive(self):
    return self.hp > 0

PLAYER.is_alive = is_alive
ENEMY.is_alive = is_alive