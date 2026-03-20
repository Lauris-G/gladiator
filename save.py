#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## save.py
##

import json
import os

def save_player(player):
    os.makedirs("saves", exist_ok=True)

    data = {
        "name": player.name
    }

    with open("saves/save.json", "w") as file:
        json.dump(data, file)

def load_player(player):
    try:
        with open("saves/save.json", "r") as file:
            data = json.load(file)
            player.name = data.get("name", "")
            return "main"
    except FileNotFoundError:
        return "pseudo"