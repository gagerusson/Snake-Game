import pygame
import sys
import time
import random

pygame.init()

difficulty = 20

WIDTH = 720
HEIGHT = 480
BLOCKSIZE = 20

pygame.display.set_caption('Snake by Gage')
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green1 = pygame.Color(0, 255, 0)
green2 = pygame.Color(50, 200, 0)


timer = pygame.time.Clock()

snake_pos = [360, 240]
snake_body = [[360, 240], [360-BLOCKSIZE, 240], [360-(BLOCKSIZE*2), 240]]

food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

SCORE = 0

# def draw_window(color1, color2):
#     for x in range(0, int(WIDTH)):
#         for y in range(0, int(HEIGHT)):
#             if (x + y) % 2 == 0:
#                 rect = pygame.Rect((x*BLOCKSIZE, y*BLOCKSIZE), (BLOCKSIZE, BLOCKSIZE))
#                 pygame.draw.rect(WINDOW, green1, rect)
#             else:
#                 rect2 = pygame.Rect((x*BLOCKSIZE, y*BLOCKSIZE), (BLOCKSIZE, BLOCKSIZE))
#                 pygame.draw.rect(WINDOW, green2, rect2)          

def game_over():
    font = pygame.font.SysFont(None, 90)
    surface = font.render('YOU DIED', True, red)
    rect = surface.get_rect()
    rect.midtop = (WIDTH/2, HEIGHT/4)
    WINDOW.fill(black)
    WINDOW.blit(surface, rect)
    score(False, red, 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def score(in_game, color, size):
    if in_game:
        font = pygame.font.SysFont(None, size)
    else:
        font = pygame.font.SysFont(None, 75)
    surface = font.render('Score : ' + str(SCORE), True, color)
    rect = surface.get_rect()
    if in_game:
        rect.midtop = (75, 5)
    else:
        rect.midtop = (WIDTH/2, HEIGHT/1.5)
    WINDOW.blit(surface, rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    #change snakes direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    #eat food
    snake_body.insert(0, list(snake_pos))
    if ((snake_pos[0] >= food_pos[0] - 10 and snake_pos[0] <= food_pos[0]) or (snake_pos[0] <= food_pos[0] + 10 and snake_pos[0] >= food_pos[0])) and ((snake_pos[1] >= food_pos[1] - 10 and snake_pos[1] <= food_pos[1]) or (snake_pos[1] <= food_pos[1] + 10 and snake_pos[1] >= food_pos[1])):
        SCORE += 1
        if SCORE % 2 == 0 and SCORE != 0:
            difficulty += 1
        food_spawn = False
    else:
        snake_body.pop()
    # if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
    #     SCORE += 1
    #     food_spawn = False
    # else:
    #     snake_body.pop()

    #spawn food
    if not food_spawn:
        food_pos = [random.randrange(10, (WIDTH//10)) * 10, random.randrange(10, (HEIGHT//10)) * 10]
    food_spawn = True

    #draw screen
    WINDOW.fill(green1)
    # draw_window(green1, green2)
    
    #draw snake
    for pos in snake_body:
        pygame.draw.rect(WINDOW, black, pygame.Rect(pos[0], pos[1], 20, 20))

    #draw food
    pygame.draw.rect(WINDOW, red, pygame.Rect(food_pos[0], food_pos[1], 20, 20))

    #edge detection
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over()

    #tail collision detection
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    #update score
    score(True, white, 50)

    pygame.display.update()

    timer.tick(difficulty)
