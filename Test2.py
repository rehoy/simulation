import sys
import pygame
from pygame.locals import*
import math


def main():

    width = 1000
    height = 600
    color = (0, 0, 0)
    line_color = (255, 255, 255)

    screen = pygame.display.set_mode((width, height))
    screen.fill(color)

    x1 = 300
    x2 = 400
    y1 = 300
    y2 = 290

    print(math.degrees(math.atan2(y2 - y1, x2 - x1)))
    while True:

        pygame.draw.line(screen, line_color, (x1, y1), (x2, y2))
        pygame.draw.circle(screen, (255, 255, 255), (200, 200), 10, 0)

        pygame.display.flip()
        screen.fill(color)

        for events in pygame.event.get():
            if events.type == QUIT:

                sys.exit(0)


main()
