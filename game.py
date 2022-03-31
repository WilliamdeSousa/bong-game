import pygame, sys
from pygame.locals import *


class Objeto:
    def __init__(self):
        self.x = 0
        self.y = 0


class Body(Objeto):
    def __init__(self, size=(100, 100), color=(255, 255, 255)):
        super().__init__()
        self.color = list
        self.width = int
        self.height = int
        self.rect = list
        self.set_values(size, color)

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.set_rect()

    def set_values(self, size: list, color: list):
        self.width = size[0]
        self.height = size[1]
        self.color = color
        self.set_rect()

    def set_rect(self):
        self.rect = [self.x, self.y, self.width, self.height]


class Vetor(Objeto):
    def __init__(self):
        super().__init__()


class Dinamic(Objeto):
    def __init__(self):
        super().__init__()
        self.body = Body()
        self.vetor = Vetor()

    def update(self):
        self.x += self.vetor.x
        self.y += self.vetor.y
        self.body.set_rect()


class Player(Dinamic):
    def __init__(self):
        super().__init__()
