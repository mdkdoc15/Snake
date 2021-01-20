import pygame 
import random

# Total Size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
# Allow us to divide the screen into 20x20 squres
GRIDSIZE = 20
GRID_WIDTH = int(SCREEN_WIDTH/GRIDSIZE)
GRID_HEIGHT = int(SCREEN_HEIGHT/GRIDSIZE)

# Movement of the snake [X , Y]
UP = [0,-1]
DOWN = [1,0]
LEFT = [-1,0]
RIGHT = [1,0]

BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (88,73,130)
LIGHT_GREEN = (180,255,171)
DARK_GREEN = (132,255,171)


class Snake(object):
    def __init__(self):
        self.positions = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
        self.direction = random.choice([UP,DOWN,LEFT, RIGHT])
        self.size = 1
        self.score = 0
        self.color = PURPLE

    def get_head_pos(self):
        return self.positions[0]
    
    def move(self):
        print(self.positions)
        print("________________")
        current = self.get_head_pos()
        new = (current[0] + self.direction[0] * GRIDSIZE, current[1] + self.direction[1] * GRIDSIZE)
        if new in self.positions:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.size:
                self.positions.pop()

    def turn(self, direction):
        pass
    def draw(self, surface):
        for body in self.positions:
            r = pygame.Rect(body[0], body[1], GRIDSIZE, GRIDSIZE)
            pygame.draw.rect(surface, self.color, r)

    def reset(self):
        self.positions = [(GRID_WIDTH/2, GRID_HEIGHT/2)]
        self.size = 1
        self.score = 0
    def movement(self):
        pass


class Food(object):
    def __init__(self):
        pass
    def get_postion(self):
        pass
    def randomize_position(self):
        pass

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
    #Initilize all images
    icon = pygame.image.load('Images/snake.png')
    body_icon = pygame.image.load('Images/circle.png')

    #Set Icon
    pygame.display.set_icon(icon)

    #Set Titile
    pygame.display.set_caption('Snake')
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    
    drawGrid(surface)

    snake = Snake()

    game_over = False
    while not game_over:
        clock.tick(10)
        screen.fill(WHITE) 
        snake.draw(surface)
        snake.move()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
        screen.blit(surface, (0,0))
        pygame.display.update()


if __name__ == "__main__":
    main()
