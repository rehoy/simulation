import pygame
import random


class Particle:

    def __init__(self, x, y, r, brett):
        self.x = x
        self.y = y
        self.v = pygame.Vector2(random.randint(-3, 3), random.randint(-3, 3))
        self.r = r
        self.brett = brett
        self.color = (255, 255, 255)

    def draw(self):
        pygame.draw.circle(self.brett.screen, self.color,
                           (self.x, self.y), self.r, 0)

    def update(self):

        self.random()
        self.x += int(self.v.x)
        self.y += int(self.v.y)
        self.check_edges()
        # self.y += int(self.v.y)

    def check_edges(self):
        if self.x > self.brett.width:
            self.x = 0
        if self.x < 0:
            self.x = self.brett.width

        if self.y > self.brett.height:
            self.y = 0
        if self.y < 0:
            self.y = self.brett.height

    def random(self):
        max_speed = 3
        self.v = self.v + \
            pygame.Vector2(random.randint(-1, 1), random.randint(-1, 1))
        if self.v.length() > max_speed:
            self.v.scale_to_length(max_speed)
