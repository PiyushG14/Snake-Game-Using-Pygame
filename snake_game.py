#Draw a moving snake

import pygame
import random

class Snake():
    def __init__(self):
        #Initialize the attributes
        self.length = 3
        self.position = [(WIDTH//2, HEIGHT//2), (WIDTH//2, HEIGHT//2 + gridsize), (WIDTH//2, HEIGHT//2 + 2*gridsize)  ]   #Array of co-ordinates
        self.color = (0, 0, 255)
        self.direction = up
        self.score = 0
        
    def drawSnake(self, window):
        #Draw a rect for every coordinate in position
        for block in self.position:
            pygame.draw.rect(window, self.color, (block[0], block[1], gridsize, gridsize))
            
    def movement(self):
        head = self.position[0]
        x,y = self.direction
        #Move in that direction
        next = ((head[0]+x*gridsize)%WIDTH , (head[1]+y*gridsize)%HEIGHT)
        #check_game_end()
        
        self.position.insert(0,next)
        self.position.pop()
    
    def check_game_end(self):
        pass
        
    
    def change_direction(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not self.direction == down:
                        self.direction = up                    
                elif event.key == pygame.K_DOWN:
                    if not self.direction == up:
                        self.direction = down  
                elif event.key == pygame.K_LEFT:
                    if not self.direction == right:
                        self.direction = left  
                elif event.key == pygame.K_RIGHT:
                    if not self.direction == left:
                        self.direction = right  
       
        
    
    
    
class Food():
    def __init__(self):
        pass
    

WIDTH = 400
HEIGHT = 400

grids = 20

gridsize = WIDTH//grids

#Defining directions
up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

def setBackground(window):
    window.fill((175, 215, 70))
    #pygame.display.update()

def main():    
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))  #pygame window
    pygame.display.set_caption("Snake Game")
    setBackground(window)
    
    snake = Snake()
    food = Food()
    
    while True:
        clock.tick(10)    #12 frames per second
        #pygame.time.delay(50)
    
        snake.movement()
        
        setBackground(window)
        
        snake.drawSnake(window)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                return   
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not snake.direction == down:
                        snake.direction = up     
                        
                elif event.key == pygame.K_DOWN:
                    if not snake.direction == up:
                        snake.direction = down  

                elif event.key == pygame.K_LEFT:
                    if not snake.direction == right:
                        snake.direction = left  

                elif event.key == pygame.K_RIGHT:
                    if not snake.direction == left:
                        snake.direction = right  

        pygame.display.update()
    
    return
   
main()
