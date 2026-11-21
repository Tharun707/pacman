import pygame

WIDTH = 600
HEIGHT = 600
SPEED = 4
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Pacman")
    clock = pygame.time.Clock()

    x,y = WIDTH//2 , HEIGHT//2 #to init the pacman in the middle of the screen
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x-=SPEED
        if keys[pygame.K_RIGHT]:
            x+=SPEED
        if keys[pygame.K_UP]:
            y-=SPEED
        if keys[pygame.K_DOWN]:
            y+=SPEED


        screen.fill((0,0,0))
        pygame.draw.circle(screen ,(255,255,0),(x,y),20)
        pygame.display.flip()

        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()