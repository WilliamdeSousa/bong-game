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

    player_1 = game.Player()
    player_2 = game.Player()
    ball = game.Dinamic()

    player_1.body.set_values(PLAYERS_SIZE, PLAYER_1_COLOR)
    player_2.body.set_values(PLAYERS_SIZE, PLAYER_2_COLOR)
    ball.body.set_values(BALL_SIZE, BALL_COLOR)

    ball.x = BALL_POSITION[0]
    ball.y = BALL_POSITION[1]
    player_1.x = PLAYER_1_X
    player_1.y = PLAYER_1_Y
    player_2.x = PLAYER_2_X
    player_2.y = PLAYER_2_Y


def objects():
    global objects_list
    objects_list = [player_1, player_2, ball]

    update_objects()
    draw_objects()


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
    objects()
    pygame.display.flip()


def bg_update():
    pygame.draw.rect(screen, BG_COLOR, (0, 0, WIDTH, HEIGHT))


# GAME
screen = game_init()

while True:
    pygame.time.delay(6)
    for event in pygame.event.get():
        if event.type == QUIT:
            quit(0)
        if event.type == KEYDOWN:
            if event.key == K_KP_ENTER or event.key == KSCAN_KP_ENTER:
                ball.vetor.x = ball.vetor.y = BALL_SPEED
            if event.key == K_RIGHT:
                player_2.keys.add('RIGHT')
            if event.key == K_LEFT:
                player_2.keys.add('LEFT')
            if event.key == K_d:
                player_1.keys.add('RIGHT')
            if event.key == K_a:
                player_1.keys.add('LEFT')

    game_update()
