#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## save.py
##

import json
import os

def save_player(game_state):
    os.makedirs("saves", exist_ok=True)
    inventory = []
    for obj in game_state.shop_weapons:
        inventory.append({
            "name": obj.name,
            "owned": obj.owned,
            "level": obj.level,
            "attack": obj.attack,
            "defense": obj.defense,
        })
    data = {
        "name": game_state.player.name,
        "win": game_state.win,
        "gold": game_state.player.gold,
        "weapon": game_state.player.weapon,
        "inventory": inventory,
    }
    with open("saves/save.json", "w") as file:
        json.dump(data, file)

def load_player(game_state):
    try:
        with open("saves/save.json", "r") as file:
            data = json.load(file)
            game_state.player.name = data.get("name", "")
            game_state.win = data.get("win", 0)
            game_state.player.gold = data.get("gold", 0)
            game_state.player.weapon = data.get("weapon", "sword")
            for saved in data.get("inventory", []):
                for obj in game_state.shop_weapons:
                    if obj.name == saved["name"]:
                        obj.owned   = saved["owned"]
                        obj.level   = saved["level"]
                        obj.attack  = saved["attack"]
                        obj.defense = saved["defense"]
            return "main"
    except FileNotFoundError:
        return "pseudo"