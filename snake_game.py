#Game end condition

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
        if self.position[0] in self.position[1:]:
            print("game end")            
            self.__init__()
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
        self.position = (random.randint(0, WIDTH)//grids*grids, random.randint(0, WIDTH)//grids*grids)
        self.color = (0, 0, 0)
        
    def draw_food(self,window):
        pygame.draw.rect(window, self.color, (self.position[0], self.position[1], gridsize, gridsize))
        #print((self.position[0]*grids, self.position[1]*grids, gridsize, gridsize))


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

def main():    
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))  #pygame window
    pygame.display.set_caption("Snake Game")
    setBackground(window)
    
    snake = Snake()
    food = Food()
    
    while True:
        clock.tick(12)    #12 frames per second
        snake.movement()
        snake.check_game_end()
        setBackground(window)
        
        snake.drawSnake(window)
        food.draw_food(window)
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
                        
        #Food Eating code
        if food.position == snake.position[0]:
            print("Food Eaten")
            snake.length += 1
            snake.position.append((2*snake.position[-1][0] - snake.position[-2][0], \
                                  2*snake.position[-1][1] - snake.position[-2][1]))
            food.__init__()

        pygame.display.update()
    
    return
   
main()
