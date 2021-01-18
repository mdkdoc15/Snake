import pygame 

def main():
    pygame.init()

    #Initilize all images
    icon = pygame.image.load('Images/snake.png')
    body_icon = pygame.image.load('Images/circle.png')

    #Set Icon
    pygame.display.set_icon(icon)

    #Set Titile
    pygame.display.set_caption('Snake')

    SCREEN_SIZE =500
    screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))

    game_over = False
    while not game_over:
        screen.fill((255,255,255)) 

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
        pygame.display.update()


if __name__ == "__main__":
    main()
