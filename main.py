import pygame 
import random


# Total Size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
# Allow us to divide the screen into 20x20 squres
GRIDSIZE = 20
GRID_WIDTH = int(SCREEN_WIDTH/GRIDSIZE)
GRID_HEIGHT = int(SCREEN_HEIGHT/GRIDSIZE)


#Initilize all images
ICON = pygame.image.load('Images/snake.png')
BODY_IMG = pygame.image.load('Images/circle.png')
BODY_IMG = pygame.transform.scale(BODY_IMG, (GRIDSIZE, GRIDSIZE))
FOOD_IMG = pygame.image.load('Images/apple.png')
FOOD_IMG = pygame.transform.scale(FOOD_IMG, (GRIDSIZE,GRIDSIZE))

# Movement of the snake [X , Y]
UP = [0,-1]
DOWN = [0,1]
LEFT = [-1,0]
RIGHT = [1,0]

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW =(255,255,153)
PURPLE = (88,73,130)
LIGHT_GREEN = (180,255,171)
DARK_GREEN = (132,255,171)


class Snake(object):
    def __init__(self):
        self.positions = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])
        self.size = 1
        self.score = 0
        self.color = PURPLE

    def get_head_pos(self):
        return self.positions[0]
    
    def move(self):
        current = self.get_head_pos()
        new = (current[0] + self.direction[0] * GRIDSIZE, current[1] + self.direction[1] * GRIDSIZE)
        if new in self.positions:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.size:
                self.positions.pop()
        if(self.positions[0][0] > SCREEN_WIDTH or self.positions[0][0] < 0 or self.positions[0][1] > SCREEN_HEIGHT or self.positions[0][1] < 0):
            self.reset()

    def turn(self, new_direction):
        if not (self.size > 1 and self.direction[0] * - 1 == new_direction[0] and self.direction[1]*-1 == new_direction[1]):
            self.direction = new_direction
        
    def draw(self, surface):
        for body in self.positions:
            surface.blit(BODY_IMG, body)

    def reset(self):
        self.positions = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
        self.size = 1
        self.score = 0
        self.direction = random.choice([UP,DOWN,LEFT,RIGHT])

    


class Food(object):
    def __init__(self):
        self.position = [0,0]
        self.color = YELLOW
        self.randomize_position()
    def get_postion(self):
        return self.position
    def randomize_position(self):
        self.position = (random.randint(0,GRID_WIDTH-1) * GRIDSIZE, random.randint(0,GRID_HEIGHT-1) * GRIDSIZE)
    def draw(self, surface):
        surface.blit(FOOD_IMG, self.position)

def drawGrid(surface):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            r = pygame.Rect(x*GRIDSIZE, y *GRIDSIZE, GRIDSIZE, GRIDSIZE)
            if (x + y) % 2 == 0:
                pygame.draw.rect(surface, LIGHT_GREEN, r)
            else:
                pygame.draw.rect(surface,DARK_GREEN, r)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    #Set Icon
    pygame.display.set_icon(ICON)

    #Set Titile
    pygame.display.set_caption('Snake')
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    
    drawGrid(surface)

    snake = Snake()
    food = Food()

    game_over = False
    while not game_over:
        #Control the game time
        clock.tick(10)
        
        # Add items to the screen
        screen.fill(WHITE) 
        drawGrid(surface)

        #Check for events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)

        # Update the snake
        snake.move()
        snake.draw(surface)
        
        # Add the food to the screen
        food.draw(surface)

        if(snake.get_head_pos() == food.get_postion()):
            snake.score += 1
            snake.size += 1
            print("Score :", snake.score)
            food.randomize_position()


        
        # Update the screen
        screen.blit(surface, (0,0))
        pygame.display.update()


if __name__ == "__main__":
    main()
