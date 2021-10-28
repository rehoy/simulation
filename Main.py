# eneste som trengs for aa gjoere det mer generelt er aa fjerne
# screen i konstruktoeren i Tentacle og Segment

import sys
import pygame
from pygame.locals import*
import math
from Segment import Segment
from Tentacle import Tentacle
# info = pygame.display.Info()
width = 1200
height = 600
Color_screen = (0, 0, 0)
screen = pygame.display.set_mode((width, height))
# paramenter 1 er hvor mange deler, par. 2 er lengden på tentakkelen
t = Tentacle(150, 1000, screen)
s = Segment(100, 100, 500, screen)


def main():

    screen.fill(Color_screen)

    while True:
        mx, my = pygame.mouse.get_pos()

        t.follow(mx, my)
        s.follow(mx, my)
        s.update()
        s.draw()
        t.run()

        pygame.display.flip()
        screen.fill(Color_screen)

        for events in pygame.event.get():
            if events.type == QUIT:

                sys.exit(0)


main()
