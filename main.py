import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Input
        updatable.update(dt)

        for a in asteroids:
            if a.collide(player):
                print("Game over!")
                pygame.QUIT
                return
            for s in shots:
                if s.collide(a):
                    a.split()
                    s.kill()

        # Rendering
        screen.fill((0,0,0))

        for d in drawable:
            d.draw(screen)
        # drawable.draw(screen)
        
        pygame.display.flip()
        
        dt = (clock.tick(144) / 1000)

if __name__ == "__main__": 
    main()

    