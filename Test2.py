import sys
import pygame
from pygame.locals import*
import math
from Segment import Segment


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

    s = Segment(x1, y1, 100, screen)
    print(s.vinkel)

    print(math.degrees(math.atan2(y2 - y1, x2 - x1)))
    while True:
        mx, my = pygame.mouse.get_pos()

        v2x, v2y = s.seek(mx, my)
        # s.move()
        # s.update()
        s.draw()
        # pygame.draw.line(screen, line_color, (x1, y1), (x2, y2))
        pygame.draw.circle(screen, (255, 255, 255), (v2x, v2y), 10, 0)
        pygame.draw.line(screen, (255, 0, 0), (x1, y1), (x1 + v2x, y1 + v2y))

        pygame.display.flip()
        screen.fill(color)

        for events in pygame.event.get():
            if events.type == QUIT:

                sys.exit(0)


main()
