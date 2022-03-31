import pygame
import game
from pygame.locals import *
from constants import *

global player_1
global player_2
global ball
global objects_list


def objects_init():
    global player_1
    global player_2
    global ball

    global objects_list

    player_1 = game.Player()
    player_2 = game.Player()
    ball = game.Dinamic()

    objects_list = [player_1, player_2, ball]

    player_1.body.set_values(PLAYERS_SIZE, PLAYER_1_COLOR)
    player_2.body.set_values(PLAYERS_SIZE, PLAYER_2_COLOR)
    ball.body.set_values(BALL_SIZE, BALL_COLOR)

    ball.body.set_position(BALL_POSITION[0], BALL_POSITION[1])
    player_1.body.set_position(PLAYER_1_X, PLAYER_1_Y)
    player_2.body.set_position(PLAYER_2_X, PLAYER_2_Y)

    ball.vetor.x = 1
    ball.vetor.y = 1


def update_objects():
    for obj in objects_list:
        obj.update()


def draw_objects():
    for obj in objects_list:
        pygame.draw.rect(screen, obj.body.color, obj.body.rect)


def game_init():
    pygame.init()
    objects_init()
    window = pygame.display.set_mode(SIZE)
    return window


def game_update():
    bg_update()
    update_objects()
    draw_objects()
    pygame.display.flip()


def bg_update():
    pygame.draw.rect(screen, BG_COLOR, (0, 0, WIDTH, HEIGHT))


# GAME
screen = game_init()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit(0)

    game_update()
