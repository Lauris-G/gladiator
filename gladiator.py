#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## gladiator.py
##

import pygame
import json

pygame.init()

BASE_WIDTH, BASE_HEIGHT = 1280, 720
FPS = 60

screen = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Gladiator")
game_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def save_player(player):
    data = {
        "name": player.name
    }

    with open("save.json", "w") as file:
        json.dump(data, file)

def load_player(player):
    global current_menu

    try:
        with open("save.json", "r") as file:
            data = json.load(file)
            player.name = data.get("name", "")
            current_menu = "main"
    except FileNotFoundError:
        current_menu = "pseudo"

class PLAYER:
    def __init__(self, player_name=""):
        self.name = player_name

player = PLAYER()
load_player(player)

class MENU:
    def __init__(self, name, background=None, fct_click=None, fct_printing=None, buttons=None):
        self.name = name
        self.background = background
        self.fct_click = fct_click
        self.fct_printing = fct_printing
        self.buttons = buttons if buttons else []

    def is_clicked(self, event, mouse_pos):
        if self.fct_click != None:
            self.fct_click(event, mouse_pos)

    def draw(self, game_surface):
        if self.fct_printing != None:
            self.fct_printing(game_surface)

class BUTTON:
    def __init__(self, rect, background=None, hovered_background=None, fct_click=None):
        self.rect = pygame.Rect(rect)
        self.background = background
        self.hovered = hovered_background
        self.fct_click = fct_click

def start_game():
    print("Démarrer le jeu !")

def open_shop():
    global current_menu
    current_menu = "shop"

def back_to_main():
    global current_menu
    current_menu = "main"

input_rect = pygame.Rect(450, 300, 380, 60)

def click_in_pseudo(event, mouse_pos):
    global current_menu

    if event.type == pygame.MOUSEBUTTONDOWN:
        pass
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            player.name = player.name[:-1]
        elif event.key == pygame.K_RETURN:
            print("Pseudo choisi :", player.name)
            save_player(player)
            current_menu = "main"
        else:
            if len(player.name) < 12:
                player.name += event.unicode

def draw_pseudo(game_surface):
    pygame.draw.rect(game_surface, (220,220,220), input_rect)
    text_surface = font.render(player.name, True, (0,0,0))
    game_surface.blit(text_surface, (input_rect.x + 10, input_rect.y + 15))
    title = font.render("Entrez votre pseudo :", True, (255,255,255))
    game_surface.blit(title, (450, 250))

def draw_main_menu(game_surface):
    text_surface = font.render(player.name, True, (225,225,225))
    game_surface.blit(text_surface, (10, 15))

def click_in_shop(event, mousepos):
    pass

pseudo_menu = MENU("pseudo", fct_click=click_in_pseudo, fct_printing=draw_pseudo)

shop_menu = MENU("shop", fct_click=click_in_shop)

main_menu = MENU("main", fct_printing=draw_main_menu)

menus = {"pseudo": pseudo_menu, "main": main_menu, "shop": shop_menu}

running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    scale_x = BASE_WIDTH / screen.get_width()
    scale_y = BASE_HEIGHT / screen.get_height()
    mouse_pos_scaled = (mouse_x * scale_x, mouse_y * scale_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        menus[current_menu].is_clicked(event, mouse_pos_scaled)
    
    game_surface.fill((50,50,50))

    menus[current_menu].draw(game_surface)
    
    scaled = pygame.transform.scale(game_surface, screen.get_size())
    screen.blit(scaled, (0,0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()