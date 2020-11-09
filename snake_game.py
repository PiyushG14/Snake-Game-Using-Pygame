#pygame screen setup

import pygame
import random

class Snake():
    def __init__(self):
        pass
    
    
    
class Food():
    def __init__(self):
        pass
    
def setBackground(window):
    window.fill((175, 215, 70))
    pygame.display.update()
    
def main():    
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))  #pygame window
    pygame.display.set_caption("Snake Game")
    setBackground(window)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return   
    
    return
   
main()
