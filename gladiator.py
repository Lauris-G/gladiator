#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## gladiator.py
##

import pygame
from buttons import *
from fight import *
from save import *
from menu import *

pygame.init()

BASE_WIDTH, BASE_HEIGHT = 2560, 1440
FPS = 60

screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Gladiator")
game_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Californian FB", 56, bold=False)
pygame.mixer.init(frequency=44100, size=-16, channels=2)

click_sound = pygame.mixer.Sound("assets/click1.wav")
pygame.mixer.Sound.set_volume(click_sound, 0.1)
hover_sound  = pygame.mixer.Sound("assets/hovered1.wav")
pygame.mixer.Sound.set_volume(hover_sound, 0.1)
attack_sound  = pygame.mixer.Sound("assets/attack.mp3")
pygame.mixer.Sound.set_volume(attack_sound, 0.1)

btn_play = pygame.image.load("assets/jouer.png").convert_alpha()
btn_play = pygame.transform.scale(btn_play, (900, 400))
btn_play_hover = pygame.image.load("assets/jouerflm.png").convert_alpha()
btn_play_hover = pygame.transform.scale(btn_play_hover, (900, 400))

btn_shop = pygame.image.load("assets/magasin.png").convert_alpha()
btn_shop = pygame.transform.scale(btn_shop, (900, 400))
btn_shop_hover = pygame.image.load("assets/magasinflm.png").convert_alpha()
btn_shop_hover = pygame.transform.scale(btn_shop_hover, (900, 400))

btn_quit = pygame.image.load("assets/quitter.png").convert_alpha()
btn_quit = pygame.transform.scale(btn_quit, (900, 400))
btn_quit_hover = pygame.image.load("assets/quitterflm.png").convert_alpha()
btn_quit_hover = pygame.transform.scale(btn_quit_hover, (900, 400))

FIGHT_WIDTH = 900
FIGHT_HEIGHT = 400

btn_simple = pygame.image.load("assets/simple.png").convert_alpha()
btn_simple = pygame.transform.scale(btn_simple, (FIGHT_WIDTH, FIGHT_HEIGHT))
btn_simple_hover = pygame.image.load("assets/simpleflm.png").convert_alpha()
btn_simple_hover = pygame.transform.scale(btn_simple_hover, (FIGHT_WIDTH, FIGHT_HEIGHT))

btn_special = pygame.image.load("assets/speciale.png").convert_alpha()
btn_special = pygame.transform.scale(btn_special, (FIGHT_WIDTH, FIGHT_HEIGHT))
btn_special_hover = pygame.image.load("assets/specialeflm.png").convert_alpha()
btn_special_hover = pygame.transform.scale(btn_special_hover, (FIGHT_WIDTH, FIGHT_HEIGHT))

btn_heavy = pygame.image.load("assets/puissante.png").convert_alpha()
btn_heavy = pygame.transform.scale(btn_heavy, (FIGHT_WIDTH, FIGHT_HEIGHT))
btn_heavy_hover = pygame.image.load("assets/puissanteflm.png").convert_alpha()
btn_heavy_hover = pygame.transform.scale(btn_heavy_hover, (FIGHT_WIDTH, FIGHT_HEIGHT))

btn_block = pygame.image.load("assets/contre.png").convert_alpha()
btn_block = pygame.transform.scale(btn_block, (FIGHT_WIDTH, FIGHT_HEIGHT))
btn_block_hover = pygame.image.load("assets/contreflm.png").convert_alpha()
btn_block_hover = pygame.transform.scale(btn_block_hover, (FIGHT_WIDTH, FIGHT_HEIGHT))

class GameState:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.current_menu = "pseudo"
        self.fight = None
        self.win = 0

game_state = GameState()

game_state.player = PLAYER()
game_state.enemy = ENEMY("Ennemi")
game_state.fight = FIGHT(game_state.player, game_state.enemy)

game_state.current_menu = load_player(game_state)

input_rect = pygame.Rect(900, 600, 760, 120)

def formate(n):
    return f"{n:_}".replace("_", " ")

# Pseudo menu

def draw_pseudo(game_surface):
    pygame.draw.rect(game_surface, (220,220,220), input_rect)
    text_surface = font.render(game_state.player.name, True, (0,0,0))
    game_surface.blit(text_surface, (input_rect.x + 20, input_rect.y + 30))
    title = font.render("Entrez votre pseudo :", True, (255,255,255))
    game_surface.blit(title, (900, 500))

def click_in_pseudo(event, mouse_pos, game_state):
    if event.type == pygame.MOUSEBUTTONDOWN:
        pass
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            game_state.player.name = game_state.player.name[:-1]
        elif event.key == pygame.K_RETURN:
            print("Pseudo choisi :", game_state.player.name)
            save_player(game_state)
            back_to_main(game_state)
        else:
            if len(game_state.player.name) < 12:
                game_state.player.name += event.unicode

pseudo_menu = MENU("pseudo", fct_click=click_in_pseudo, fct_printing=draw_pseudo)

# Main menu

def draw_main_menu(game_surface):
    text_surface = font.render(game_state.player.name, True, (225,225,225))
    game_surface.blit(text_surface, (20, 30))
    win_streak = font.render(f"Win: {formate(game_state.win)}", True, (225,225,225))
    game_surface.blit(win_streak, (20, 1410 - font.get_height()))
    for button in main_menu.buttons:
        button.draw(game_surface, mouse_pos_scaled)

def click_in_menu(event, mousepos, game_state):
    global current_menu

    if event.type == pygame.MOUSEBUTTONDOWN:
        for button in main_menu.buttons:
            button.click(event, mousepos)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_j:
            start_game(game_state)
        if event.key == pygame.K_ESCAPE:
            close_game(game_state)

main_menu = MENU("main", fct_printing=draw_main_menu, fct_click=click_in_menu)

# Fight menu

def draw_text_multiline(surface, text, x, y, font, color=(255,255,255), line_spacing=5):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (x, y + i * (font.get_height() + line_spacing)))

def draw_fight(game_surface):
    fight = game_state.fight
    player_hp = font.render(f"{game_state.player.name} PV: {formate(game_state.player.hp)}", True, (255,255,255))
    player_hp_rect = player_hp.get_rect(left=30, top=100)
    enemy_hp = font.render(f"{game_state.enemy.name} PV: {formate(game_state.enemy.hp)}", True, (255,255,255))
    enemy_hp_rect = enemy_hp.get_rect(right=BASE_WIDTH - 30, top=100)
    game_surface.blit(player_hp, player_hp_rect)
    game_surface.blit(enemy_hp, enemy_hp_rect)
    turn_text = font.render(f"Tour {formate(fight.turn_count)}", True, (255, 255, 255))
    turn_rect = turn_text.get_rect(centerx=BASE_WIDTH // 2, top=100)
    game_surface.blit(turn_text, turn_rect)

    if hasattr(fight, "message"):
        draw_text_multiline(game_surface, fight.message, 400, 600, font, (255,255,0))

    for button in fight_menu.buttons:
        button.draw(game_surface, mouse_pos_scaled)

    if fight.is_over():
        end_font = pygame.font.SysFont("Californian FB", font.get_height() + 15, bold=True)
        text = "Victoire !" if game_state.player.hp > 0 else "Défaite..."
        end_text = end_font.render(text, True, (255,0,0))
        end_text_rect = end_text.get_rect(centerx=BASE_WIDTH // 2, centery=BASE_HEIGHT // 2 - 150)
        game_surface.blit(end_text, end_text_rect)

def click_in_fight(event, mousepos, game_state):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if game_state.fight.is_over():
            if (game_state.player.hp > 0):
                game_state.win += 1
            back_to_main(game_state)
        for button in fight_menu.buttons:
            button.click(event, mousepos)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            back_to_main(game_state)

fight_menu = MENU("fight", fct_printing=draw_fight, fct_click=click_in_fight)

def draw_shop(game_state):
    pass

def click_in_shop(event, mousepos, game_state):
    if event.type == pygame.MOUSEBUTTONDOWN:
        pass
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            back_to_main(game_state)

shop_menu = MENU("shop", fct_click=click_in_shop, fct_printing=draw_shop)

# Init menus

menus = {"pseudo": pseudo_menu, "main": main_menu, "shop": shop_menu, "fight": fight_menu}

# Init click functions for main menu

def start_game(game_state):
    game_state.current_menu = "fight"
    if game_state.player.hp <= 0 or game_state.enemy.hp <= 0:
        game_state.player.full_heal()
        game_state.enemy.full_heal()
        game_state.fight.message = ""
        game_state.fight.turn_count = 1

def open_shop(game_state):
    game_state.current_menu = "shop"

def back_to_main(game_state):
    game_state.current_menu = "main"

# Init main menu buttons

main_menu.buttons = [
    BUTTON((830, 200, 900, 400), btn_play, btn_play_hover,
           lambda: start_game(game_state), hitbox=(850, 340, 680, 140), sound=click_sound, sound_hover=hover_sound),
    BUTTON((830, 550, 900, 400), btn_shop, btn_shop_hover,
           lambda: open_shop(game_state), hitbox=(850, 690, 680, 140), sound=click_sound, sound_hover=hover_sound),
    BUTTON((830, 900, 900, 400), btn_quit, btn_quit_hover,
           lambda: close_game(game_state), hitbox=(850, 1040, 680, 140), sound=click_sound, sound_hover=hover_sound),
]

# Init click function for fight menu

def player_action(action):
    fight = game_state.fight

    if fight.is_over():
        return
    if action == "simple":
        fight.simple_attack()
    elif action == "special":
        fight.special_attack()
    elif action == "heavy":
        fight.heavy_attack()
    elif action == "block":
        fight.block()

# Init fight menu buttons

fight_menu.buttons = [
    BUTTON((-78, 950, FIGHT_WIDTH, FIGHT_HEIGHT), btn_simple, btn_simple_hover,
           lambda: player_action("simple"), hitbox=(175, 1080, 400, 180), sound_hover=hover_sound, sound=attack_sound),
    BUTTON((534, 950, FIGHT_WIDTH, FIGHT_HEIGHT), btn_special, btn_special_hover,
           lambda: player_action("special"), hitbox=(700, 1090, 525, 120), sound_hover=hover_sound, sound=attack_sound),
    BUTTON((1146, 950, FIGHT_WIDTH, FIGHT_HEIGHT), btn_heavy, btn_heavy_hover,
           lambda: player_action("heavy"), hitbox=(1390, 1005, 405, 270), sound_hover=hover_sound, sound=attack_sound),
    BUTTON((1758, 950, FIGHT_WIDTH, FIGHT_HEIGHT), btn_block, btn_block_hover,
           lambda: player_action("block"), hitbox=(2000, 975, 400, 320), sound_hover=hover_sound, sound=attack_sound),
]

# Init close function

def close_game(game_state):
    global running

    save_player(game_state)
    running = False

# Starting game

running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    scale_x = BASE_WIDTH / screen.get_width()
    scale_y = BASE_HEIGHT / screen.get_height()
    mouse_pos_scaled = (mouse_x * scale_x, mouse_y * scale_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game(game_state)
        menus[game_state.current_menu].is_clicked(event, mouse_pos_scaled, game_state)

    game_surface.fill((50,50,50))

    menus[game_state.current_menu].draw(game_surface)

    scaled = pygame.transform.scale(game_surface, screen.get_size())
    screen.blit(scaled, (0,0))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()