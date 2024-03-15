import pygame
import g
import random
import Countries

class Hint:
    def __init__(self):
        self.img = None

    def display(self):
        Countries.buttons.off(('clear', 'try', 'minus', 'space', 'replay', 'back','hint'))
        Countries.buttons.on(('blue'))
        g.screen.fill((255,255,192))
