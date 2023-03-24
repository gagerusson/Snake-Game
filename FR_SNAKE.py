import pygame
import time
import random
 
pygame.init()

FPS = 15
WIDTH = 720
HEIGHT = 480
 
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
 
pygame.display.set_caption('Snake by Gage')
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
 
timer = pygame.time.Clock()

snake_pos = [100, 50]
 
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
fruit_spawn = True
 
direction = 'RIGHT'
turn = direction
 
SCORE = 0
 
def update_score(choice, color, font, size):   
    font = pygame.font.SysFont(font, size)
    score_surface = font.render('Score : ' + str(SCORE), True, color)     
    rect = score_surface.get_rect()
    WINDOW.blit(score_surface, rect)
     
def game_over():   
    font = pygame.font.SysFont('times new roman', 50)
    surface = font.render('Your Score is : ' + str(SCORE), True, RED)
    rect = surface.get_rect()
    rect.midtop = (WIDTH/2, HEIGHT/4)
    WINDOW.blit(surface, rect)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                turn = 'UP'
            if event.key == pygame.K_DOWN:
                turn = 'DOWN'
            if event.key == pygame.K_LEFT:
                turn = 'LEFT'
            if event.key == pygame.K_RIGHT:
                turn = 'RIGHT'
 
    if turn == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if turn == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if turn == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if turn == 'RIGHT' and direction != 'LEFT':
        turn = 'RIGHT'
 
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
 
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        SCORE += 1
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
         
    fruit_spawn = True
    WINDOW.fill(BLACK)
     
    for pos in snake_body:
        pygame.draw.rect(WINDOW, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(WINDOW, WHITE, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))
 
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
        game_over()
 
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
 
    # displaying score countinuously
    update_score(1, WHITE, 'times new roman', 20)
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    timer.tick(FPS)