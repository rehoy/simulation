# eneste som trengs for aa gjoere det mer generelt er aa fjerne
# self.screen i konstruktoeren i Tentacle og Segment

from Particle import Particle
import sys
import pygame
from pygame.locals import*
import math
from Segment import Segment
from Tentacle import Tentacle


class Spillebrett:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def main(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.color)

        particles = []

        for i in range(200):
            p = Particle(int(self.width/2), int(self.height/2), 5, self)
            particles.append(p)

        while True:

            pygame.draw.circle(self.screen, (255, 255, 255), (200, 200), 10, 0)

            for i in particles:
                i.update()
                i.draw()

            pygame.display.flip()
            self.screen.fill(self.color)

            for events in pygame.event.get():
                if events.type == QUIT:

                    sys.exit(0)
