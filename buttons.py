#!/usr/bin/env python3
##
## EPITECH PROJECT, 2026
## gladiator
## File description:
## buttons.py
##

import pygame

class BUTTON:
    def __init__(self, rect, image, hover_image=None, fct_click=None, hitbox=None, sound=None, sound_hover=None):
        self.rect = pygame.Rect(rect)
        self.image = image
        self.hover_image = hover_image
        self.fct_click = fct_click
        if hitbox:
            self.hitbox = pygame.Rect(hitbox)
        else:
            self.hitbox = self.rect
        self.sound = sound
        self.sound_hover = sound_hover
        self.hover = False

    def is_hovered(self, mouse_pos):
        return self.hitbox.collidepoint(mouse_pos)

    def draw(self, surface, mouse_pos):
        hovered = self.is_hovered(mouse_pos)
        if self.image:
            if hovered and self.sound_hover and not self.hover:
                self.sound_hover.play()
                self.hover = True
            if hovered and self.hover_image:
                surface.blit(self.hover_image, self.rect)
            else:
                if self.hover == True:
                    self.hover = False
                surface.blit(self.image, self.rect)
        else:
            if hovered and self.sound_hover and not self.hover:
                self.sound_hover.play()
                self.hover = True
            if hovered:
                pygame.draw.rect(surface, (255, 100, 100), self.hitbox)
            else:
                if self.hover == True:
                    self.hover = False
                pygame.draw.rect(surface, (100, 100, 255), self.hitbox)

    def click(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered(mouse_pos):
                if self.fct_click:
                    if self.sound:
                        self.sound.play()
                    self.fct_click()

