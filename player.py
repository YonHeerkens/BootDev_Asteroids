from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        move_forward = 0
        move_lateral = 0

        # rotation
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)

        # movement
        if keys[pygame.K_a]:
            move_lateral += 1
        
        if keys[pygame.K_d]:
            move_lateral -= 1
        
        if keys[pygame.K_w]:
            move_forward += 1
        
        if keys[pygame.K_s]:
            move_forward -= 1

        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                self.timer -= dt
            else:
                self.shoot()

        # actually move the player
        self.move(move_forward, move_lateral, dt)
    
    def move(self, move_forward, move_lateral, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        lateral = pygame.Vector2(0, 1).rotate(self.rotation - 90)

        move_direction = forward * move_forward + lateral * move_lateral

        if move_direction.length() > 0:
            move_direction = move_direction.normalize() * PLAYER_SPEED * dt

        self.position += move_direction

    def shoot(self):
        s = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        s.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOT_COOLDOWN
