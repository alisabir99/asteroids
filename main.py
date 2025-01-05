# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from shot import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)




    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()




    while True:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for member in drawable:
            member.draw(screen)
        dt = clock.tick(60)/1000
        for member in updatable:
            member.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collided(player):
                print('Game over!')
                return
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_collided(shot):
                    asteroid.split()
    
        pygame.display.flip()














if __name__ == "__main__":
    main()
