import pygame, sys
from pygame.locals import *


class Key:
    def __init__(self):
        self.keys_pressed = list()

    def add(self, key):
        self.keys_pressed.append(key)

    def remove(self, key):
        try:
            self.keys_pressed.remove(key)
        except ValueError:
            pass

    def check_move(self):
        if ('RIGHT' in self.keys_pressed and 'LEFT' in self.keys_pressed) or ('RIGHT' not in self.keys_pressed and 'LEFT' not in self.keys_pressed):
            return 'STOP'
        elif 'RIGHT' in self.keys_pressed:
            return 'RIGHT'
        elif 'LEFT' in self.keys_pressed:
            return 'LEFT'


class Objeto:
    def __init__(self):
        self.x = 0
        self.y = 0


class Body(Objeto):
    def __init__(self, size=(100, 100), color=(255, 255, 255)):
        super().__init__()
        self.color = list()
        self.width = int()
        self.height = int()
        self.rect = list()
        self.set_values(size, color)
        self.visible = True

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


class Circle:
    def __init__(self):
        self.center = list()
        self.radius = int()
        self.color = list()

    def update(self, x, y):
        self.center = [x + self.radius, y + self.radius]


class Vetor(Objeto):
    def __init__(self):
        super().__init__()
        self.speed_x = 0
        self.speed_y = 0


class Dinamic(Objeto):
    def __init__(self):
        super().__init__()
        self.colision = Body()
        self.vetor = Vetor()

    def update(self):
        self.x += self.vetor.x
        self.y += self.vetor.y
        self.colision.set_position(self.x, self.y)
        self.colision.set_rect()


class Ball(Dinamic):
    def __init__(self):
        super().__init__()
        self.colision.visible = False
        self.circle = Circle()
        self.border_left = self.x
        self.border_right = self.x + self.colision.width
        self.border_up = self.y
        self.border_down = self.y + self.colision.height

    def update(self):
        super().update()
        self.circle.update(self.x, self.y)
        self.border_left = self.x
        self.border_right = self.x + self.colision.width
        self.border_up = self.y
        self.border_down = self.y + self.colision.height

    def colision_with(self, obj):
        if self.check_colision_up(obj) and self.check_colision_down(obj) and self.check_colision_right(obj) and self.check_colision_left(obj):
            return True
        else:
            return False

    def check_colision_up(self, obj):
        if self.border_up <= obj.colision.y + obj.colision.height:
            return True
        else:
            return False

    def check_colision_down(self, obj):
        if self.border_down >= obj.colision.y:
            return True
        else:
            return False

    def check_colision_right(self, obj):
        if self.border_right >= obj.colision.x:
            return True
        else:
            return False

    def check_colision_left(self, obj):
        if self.border_left <= obj.colision.x + obj.colision.width:
            return True
        else:
            return False


class Player(Dinamic):
    def __init__(self):
        super().__init__()
        self.keys = Key()

    def update(self):
        super().update()
        self.check_events()

    def check_events(self):
        self.check_move()

    def check_move(self):
        if self.keys.check_move() == 'RIGHT':
            self.vetor.x = self.vetor.speed_x
        elif self.keys.check_move() == 'LEFT':
            self.vetor.x = -self.vetor.speed_x
        elif self.keys.check_move() == 'STOP':
            self.vetor.x = 0
