import pygame
from pygame import font
import game
from time import sleep
from pygame.locals import *
from constants import *
from random import choice

global player_1
global player_2
global ball
global objects_list
global game_stoped
global colision_sound
global point_sound
global win_game_sound
global music

score = [0, 0]
speed = BALL_SPEED


def win_game(player):
    win_game_mensagem(player)
    win_game_sound.play()


def win_game_mensagem(player):
    pygame.font.init()
    txt = f'JOGADOR {player} GANHOU!'
    fonte = font.get_default_font()
    fontesys = font.SysFont(fonte, 80)
    win_game_text = fontesys.render(txt, 1, (255, 255, 255))
    screen.blit(win_game_text, (CENTER_X - 310, CENTER_Y - 25))


def sounds_init():
    global colision_sound
    global point_sound
    global win_game_sound
    global music

    pygame.mixer.init()
    colision_sound = pygame.mixer.Sound(r'colision sound.wav')
    colision_sound.set_volume(0.1)
    point_sound = pygame.mixer.Sound(r'point sound.wav')
    point_sound.set_volume(0.1)
    win_game_sound = pygame.mixer.Sound(r'win-game-sound.wav')
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()


def hub():
    player_1_score_text = f'P1 = {score[0]}'
    player_2_score_text = f'P2 = {score[1]}'
    draw_text(player_1_score_text, (50, 50))
    draw_text(player_2_score_text, (50, HEIGHT - 80))


def draw_text(txt, pos, color=(255, 255, 255)):
    pygame.font.init()
    fonte = font.get_default_font()
    fontesys = font.SysFont(fonte, 40)
    scoretxt = fontesys.render(txt, 1, color)
    screen.blit(scoretxt, pos)


def stop_game():
    sleep(STOP_TIME)

    game_init()


def objects_init():
    global player_1
    global player_2
    global ball

    player_1 = game.Player()
    player_2 = game.Player()
    ball = game.Ball()

    player_1.colision.set_values(PLAYERS_SIZE, PLAYER_1_COLOR)
    player_2.colision.set_values(PLAYERS_SIZE, PLAYER_2_COLOR)
    ball.colision.set_values([BALL_RADIUS * 2, BALL_RADIUS * 2], BALL_COLOR)

    ball.x = BALL_POSITION[0]
    ball.y = BALL_POSITION[1]
    player_1.x = PLAYER_1_X
    player_1.y = PLAYER_1_Y
    player_2.x = PLAYER_2_X
    player_2.y = PLAYER_2_Y

    player_1.vetor.speed_x = player_2.vetor.speed_x = PLAYER_SPEED
    ball.vetor.speed_x = ball.vetor.speed_y = BALL_SPEED

    ball.circle.radius = BALL_RADIUS
    ball.circle.center = [ball.x + BALL_RADIUS, ball.y + BALL_RADIUS]
    ball.circle.color = BALL_COLOR


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
        if obj.colision.visible:
            pygame.draw.rect(screen, obj.colision.color, obj.colision.rect)
        try:
            pygame.draw.circle(screen, obj.circle.color, obj.circle.center, obj.circle.radius)
        except AttributeError:
            pass


def game_init():
    global game_stoped

    game_stoped = True

    pygame_inits()
    objects_init()
    window = pygame.display.set_mode(SIZE)
    return window


def pygame_inits():
    pygame.init()
    pygame.font.init()


def game_update():
    bg_update()
    objects()
    colisions()
    hub()
    screen_update()
    check_music()


def check_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()


def screen_update():
    pygame.display.flip()


def bg_update():
    pygame.draw.rect(screen, BG_COLOR, (0, 0, WIDTH, HEIGHT))


def colisions():
    global score
    # with players
    if ball.colision_with(player_2) and ball.vetor.y != -ball.vetor.speed_y:
        colision_with_player(2)
    elif ball.colision_with(player_1) and ball.vetor.y != ball.vetor.speed_y:
        colision_with_player(1)

    # with borders
    if ball.border_right >= screen.get_size()[0]:
        ball.vetor.x = -ball.vetor.speed_x
    elif ball.border_left <= 0:
        ball.vetor.x = ball.vetor.speed_x
    if ball.border_up <= 0:
        point(2)
    elif ball.border_down >= screen.get_size()[1]:
        point(1)


def colision_with_player(player):
    ball.vetor.speed_y += 0.1
    ball.vetor.speed_x += 0.1
    if player == 1:
        ball.vetor.y = ball.vetor.speed_y
    elif player == 2:
        ball.vetor.y = -ball.vetor.speed_y
    colision_sound.play()


def point(player):
    score[player-1] += 1
    if score[player-1] == 5:
        win_game_mensagem(player)
    else:
        point_sound.play()
    hub()
    screen_update()
    stop_game()


# GAME
screen = game_init()
sounds_init()

while True:
    pygame.time.delay(6)

    for event in pygame.event.get():
        if event.type == QUIT:
            quit(0)

        if event.type == KEYDOWN:
            if event.key == K_SPACE and game_stoped:
                game_stoped = False
                ball.vetor.x = choice([ball.vetor.speed_x, -ball.vetor.speed_x])
                ball.vetor.y = choice([ball.vetor.speed_y, -ball.vetor.speed_y])

            if event.key == K_RIGHT:
                player_2.keys.add('RIGHT')
            if event.key == K_LEFT:
                player_2.keys.add('LEFT')
            if event.key == K_d:
                player_1.keys.add('RIGHT')
            if event.key == K_a:
                player_1.keys.add('LEFT')

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                player_2.keys.remove('RIGHT')
            if event.key == K_LEFT:
                player_2.keys.remove('LEFT')
            if event.key == K_d:
                player_1.keys.remove('RIGHT')
            if event.key == K_a:
                player_1.keys.remove('LEFT')

    game_update()
