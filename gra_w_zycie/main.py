import pygame
import numpy
from pygame.locals import *

square_size = 10

shapey = 60
shapex = 60
board = numpy.zeros((shapex, shapey),int)

#blinker
board[5][5]=1
board[5][6]=1
board[5][7]=1

#glider
board[10][3]=1
board[11][4]=1
board[11][5]=1
board[12][3]=1
board[12][4]=1

#LWSS
board[40][31]=1
board[40][32]=1
board[40][33]=1
board[40][34]=1
board[41][30]=1
board[41][34]=1
board[42][34]=1
board[43][30]=1
board[43][33]=1

#HWSS
board[5][11]=1
board[5][12]=1
board[5][13]=1
board[5][14]=1
board[5][15]=1
board[5][16]=1
board[6][10]=1
board[6][16]=1
board[7][16]=1
board[8][10]=1
board[8][15]=1
board[9][12]=1
board[9][13]=1

#period 15
board[20][50]=1
board[21][49]=1
board[21][51]=1
board[22][48]=1
board[22][52]=1
board[23][48]=1
board[23][52]=1
board[24][48]=1
board[24][52]=1
board[25][48]=1
board[25][52]=1
board[26][48]=1
board[26][52]=1
board[27][48]=1
board[27][52]=1
board[28][49]=1
board[28][51]=1
board[29][50]=1


size = shapex*square_size, shapey*square_size
width, height = size

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

def calculate(board):
    next_board = numpy.zeros((shapex, shapey),int)
    #border is equal to 1
    for i in range(1, shapey-1):
        for j in range(1, shapex-1):
            #living_neighbours
            liv_n = board[i+1][j]+board[i+1][j-1]+board[i+1][j+1]+board[i][j+1]+board[i][j-1]+board[i-1][j]+board[i-1][j+1]+board[i-1][j-1]
            #living cell
            if(board[i][j]==1 and (liv_n==2 or liv_n==3)):
                next_board[i][j] = 1
            elif(board[i][j]==0 and liv_n==3):
                next_board[i][j] = 1
            else:
                next_board[i][j] = 0
    return next_board

def draw_board():
    for i in range(0, shapey):
        for j in range(0, shapex):
            rect = pygame.Rect(j*square_size,i*square_size,square_size,square_size)
            if(i==0 or j==0 or i==shapey-1 or j==shapex-1):
                pygame.draw.rect(screen, RED, rect)
            elif(board[i][j]==1):
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
                
            
#main loop
while running:
    draw_board()
    board = calculate(board)
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.flip()
    
pygame.quit()


                
                
            
    

