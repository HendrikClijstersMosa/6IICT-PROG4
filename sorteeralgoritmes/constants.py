import pygame

pygame.init()

class Kleur:
    ZWART = [0,0,0]
    WIT = [255,255,255]
    GROEN = [0, 255, 0]
    ROOD = [255, 0, 0]
    GRADIENT = [
        [127,127,127],
        [160,160,160],
        [192,192,192]
    ]

class Fonts:
    FONT_NORMAAL = pygame.font.SysFont('arial', 30)
    FONT_GROOT = pygame.font.SysFont('arial', 60)
