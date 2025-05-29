import pygame
from constants import *
from player import *
from asteroid import * 
from asteroidfield import *
import sys

def main():
    pygame.init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroidsGroup = pygame.sprite.Group()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroidsGroup, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    yourShip = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2, PLAYER_RADIUS)
    theField = AsteroidField()

    

    # GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for rock in asteroidsGroup:
            if rock.checkCollision(yourShip) == True:
                sys.exit("Game over!")
        for drawThing in drawable:
            drawThing.draw(screen)
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000

if __name__ == "__main__":
    main()


