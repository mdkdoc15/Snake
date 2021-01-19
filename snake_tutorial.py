#Tutorial followed from https://www.youtube.com/watch?v=9bBgyOkoBQ0

import pygame
import sys
import random

class Snake(object):
    def __init__(self):
        self.length = 1
        # Keeps track of the location of all of the memebers of the snake body
        self.positions = [((SCREEN_WIDTH/2),( SCREEN_HEIGHT/2))]
        # Randomizes which direction it will travel when it starts
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17,24,47)

    def get_head_pos(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]  * -1, point[1] *-1) == self.direction: # Prevents the snake from moving backwards if there is more than one segment on the snake
            return
        else:
            self.direction = point

    def move(self):
        cur_pos = self.get_head_pos()
        x, y = self.direction
        new = (((cur_pos[0] + x * GRIDSIZE)% SCREEN_WIDTH, (cur_pos[1] + y * GRIDSIZE)% SCREEN_HEIGHT))
        # Is the length is greater than 2(Prevents out of bounds error)
        # and is the new position the same as any other position of the snake body
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset() # Reset snake if collides with body
        else:
            # Insert the new postion  and remove the old
            self.positions.insert(0, new)
            if(len(self.positions) > self.length):
                self.positions.pop()

    def reset(self):
        # Reset the snake to its original state
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2),( SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])


    #-------------
    # Add images for the body
    # Why is there 2 draw rectangel functions
    #-------------
    def draw(self, surface):
        for p in self.positions:
            # Create the rectange of the body of the snake
            r = pygame.Rect((p[0],p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216,228), r , 1)


    def handle_keys(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
class Food(object):

    #--------
    # Impliment the food as an apple
    #--------
    def __init__(self):
        self.postion = (0,0)
        self.color = (223,163,49)
        self.randomize_pos()

    def randomize_pos(self):
        self.postion = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_WIDTH-1) * GRIDSIZE)


    #----------------
    # WHy 2 draw methods
    # -----------------
    def draw(self, surface):
        r = pygame.Rect(self.postion, (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93,216,228), r , 1)

#Total size of the screen
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

# Divides the screen up into a grid
GRIDSIZE = 20
GRID_WIDTH = SCREEN_WIDTH/ GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE


# Used to decribe movement (X, Y)
UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

# Used to create a checkerboard background
def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            # Create a rectange at that with the correct size and position
            r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE,GRIDSIZE))
            # Alternate between placing light and dark colored squares
            if(x + y) % 2 == 0:
                # Add that rectangle to the screen
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                # Add that rectangle to the screen
                pygame.draw.rect(surface,(84,194,205), r)

            

def main():
    # Start Pygame
    pygame.init()

    # Keep track of the time within the game
    clock = pygame.time.Clock()

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0 , 32)

    # Create a surface to draw onto
    surface  = pygame.Surface(screen.get_size())
    surface = surface.convert()

    drawGrid(surface)

    # Create instances of our objects
    snake = Snake()
    food = Food()

    # Used to keep track of how many apples have been eaten
    score = 0
    game_over = False

    while not game_over:
        clock.tick(10) # Creates a 10 FPS loop

        #Handle game events
        #snake.handle_keys()
        drawGrid(surface)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                #sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)

        snake.move()
        if snake.get_head_pos() == food.postion:
            snake.length += 1
            score +=1
            food.randomize_pos()

        snake.draw(surface)
        food.draw(surface)

        #text = myFont.render("Score {0}".format(score), 1 , (0,0,0))
        #Update the screen
        screen.blit(surface, (0,0))
        #screen.blit(text, (5,10))
        pygame.display.update()


main()