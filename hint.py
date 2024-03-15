import pygame
import g
import random
import Countries
import os
import utils

class Hint:
    def __init__(self):
        self.img = None
        self.cxy = (780, 150)
        self.ctr_idx = 0
        self.hint = ''

    def get_country(self):
        self.ctr_idx = random.randint(0,211)
        self.img = pygame.image.load(f"data/flags/{self.ctr_idx}.png")
        self.img = pygame.transform.scale(self.img, (400, 300))
        fname = os.path.join('data', 'countries.txt')
        f = open(fname, 'r')
        lines = f.readlines()
        self.hint = lines[self.ctr_idx]
        self.hint = self.hint[:len(self.hint)-1]

    def display(self):
        g.screen.fill((255,255,192))
        if(self.img):
            g.screen.blit(self.img,(100,50))
        utils.text_blit(
            g.screen,
            self.hint,
            g.font2,
            self.cxy,
            utils.BLACK,
            False)
