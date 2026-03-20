#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## fight.py
##

import random

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

    def full_heal(self):
        self.hp = self.maxhp

    def add_gold(self, nb):
        self.gold += nb

class ENEMY:
    def __init__(self, name):
        self.name = name
        self.maxhp = 100
        self.hp = self.maxhp
        self.attack = 8
        self.defense = 3
        self.blocking = False
    
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
        damage = self.player.attack
        self.deal_damage(self.enemy, damage)
        self.message = f"{self.player.name} attaque : {damage} dégâts"
        self.end_turn()

    def heavy_attack(self):
        if random.randint(1,100) < 70:
            damage = self.player.attack * 2
            self.deal_damage(self.enemy, damage)
            self.message = f"Attaque puissante : {damage} dégâts"
        else:
            self.message = "Attaque puissante ratée !"
        self.end_turn()

    def special_attack(self):
        weapon = self.player.weapon

        if weapon == "sword":
            damage = self.player.attack + 5
            self.deal_damage(self.enemy, damage)
            self.message = "Coup tranchant (saignement)"

        elif weapon == "spear":
            damage = self.player.attack + 3
            self.deal_damage(self.enemy, damage)
            self.message = "Estoc précis"

        elif weapon == "net":
            self.enemy.blocking = True
            self.message = "Filet : ennemi immobilisé"

        else:
            damage = self.player.attack
            self.deal_damage(self.enemy, damage)
            self.message = "Attaque spéciale"

        self.end_turn()

    def block(self):
        self.player.blocking = True
        self.message = "Vous vous préparez à bloquer"
        self.end_turn()

    def enemy_turn(self):
        if not self.enemy.is_alive():
            return

        choice = random.choice(["attack", "heavy"])

        if choice == "attack":
            damage = self.enemy.attack
            self.deal_damage(self.player, damage)
            self.message += f"\n{self.enemy.name} attaque : {damage} dégâts"

        else:
            damage = self.enemy.attack * 2
            self.deal_damage(self.player, damage)
            self.message += f"\n{self.enemy.name} attaque puissante : {damage} dégâts"

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
            self.message = "Vous avez perdu"
            self.player.hp = 0
            return True
        if self.enemy.hp <= 0:
            self.message = "Vous avez gagné"
            self.enemy.hp = 0
            return True
        return False

def is_alive(self):
    return self.hp > 0

PLAYER.is_alive = is_alive
ENEMY.is_alive = is_alive