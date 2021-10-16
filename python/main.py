import pygame
import numpy
from pygame.locals import *

import random

square_size = 20

shapey = 30
shapex = 30

size = shapex*square_size, shapey*square_size
width, height = size

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)

pygame.init()
screen = pygame.display.set_mode(size)
running = True
clock = pygame.time.Clock()

snake = [[14,14],[14,13],[14,12]]
length = 3
direction = [0,1]

def create_apple(snake):
    while(True):
        x = random.randrange(0,shapex)
        y = random.randrange(0,shapey)
        if([y,x] not in snake):
            return [y,x]

def draw_apple(posy, posx):
    rect = pygame.Rect(posy*square_size,posx*square_size,square_size,square_size)
    pygame.draw.rect(screen, RED, rect)

def draw_snake(direction, snake, length):
    for x in snake:
        rect = pygame.Rect(x[0]*square_size,x[1]*square_size,square_size,square_size)
        pygame.draw.rect(screen, BLACK, rect)
    newsnake = []
    for i in range(length):
        if(i==0):
            newsnake.append([snake[0][0]+direction[1],snake[0][1]+direction[0]])
        else:
            newsnake.append(snake[i-1])
    return newsnake

apple = create_apple(snake)
while running:
    screen.fill(WHITE)
    snake = draw_snake(direction,snake,length)
    if(snake[0][1] == apple[1] and snake[0][0]==apple[0]):
        print("A")
        length+=1
        apple = create_apple(snake)
    draw_apple(apple[0],apple[1])
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and direction != [0,1]:
        direction = [0,-1]
    if keys_pressed[pygame.K_RIGHT] and direction != [0,-1]:
        direction = [0,1]
    if keys_pressed[pygame.K_UP] and direction != [1, 0]:
        direction = [-1,0]
    if keys_pressed[pygame.K_DOWN] and direction != [-1,0]:
        direction = [1,0]
    if snake[0][0] < 0 or snake[0][0] > shapey or snake[0][1] < 0 or snake[0][1] > shapex:
        running = False
    clock.tick(20)
    pygame.display.flip()
    
pygame.quit()