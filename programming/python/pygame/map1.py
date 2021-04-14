import pygame
from pygame.locals import *
import sys



pygame.init()                                               
screen = pygame.display.set_mode((600, 400))                
pygame.display.set_caption("GAME")                          

while (1):
    screen.fill((255,255,255))                                    
    pygame.draw.line(screen, (0,95,0), (0,0), (80,80), 5)  
    pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50),5)   
    #pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50))    
    pygame.draw.ellipse(screen,(0,100,0),(50,50,200,100),5) 
    #pygame.draw.ellipse(screen,(0,100,0),(50,50,200,100))    
    pygame.display.update()                                
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:                              
            pygame.quit()                                   
            sys.exit()
