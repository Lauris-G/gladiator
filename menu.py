#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## menu.py
##

class MENU:
    def __init__(self, name, background=None, fct_click=None, fct_printing=None, buttons=None):
        self.name = name
        self.background = background
        self.fct_click = fct_click
        self.fct_printing = fct_printing
        self.buttons = buttons if buttons else []

    def is_clicked(self, event, mouse_pos, game_state):
        if self.fct_click != None:
            self.fct_click(event, mouse_pos, game_state)

    def draw(self, game_surface):
        if self.fct_printing != None:
            self.fct_printing(game_surface)