import pygame
import os

def import_skin(folder):
    skin = []
    for file in os.listdir(folder):
        skin.append(pygame.image.load(folder + '\\' + file))
    return skin

