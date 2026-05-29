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

    data = {
        "name": game_state.player.name,
        "win": game_state.win
    }

    with open("saves/save.json", "w") as file:
        json.dump(data, file)

def load_player(game_state):
    try:
        with open("saves/save.json", "r") as file:
            data = json.load(file)
            game_state.player.name = data.get("name", "")
            game_state.win = data.get("win", "")
            return "main"
    except FileNotFoundError:
        return "pseudo"