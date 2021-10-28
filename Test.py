# eneste som trengs for aa gjoere det mer generelt er aa fjerne
# screen i konstruktoeren i Tentacle og Segment

from Particle import Particle
import sys
import pygame
from pygame.locals import*
import math
from Segment import Segment
from Tentacle import Tentacle
from Spillebrett import Spillebrett
width = 1300
height = 800
Color_screen = (0, 0, 0)

v1 = pygame.Vector2(5, 5)
v2 = pygame.Vector2(10, 10)
v3 = v1 + v2
print(v3.x)

brett = Spillebrett(width, height, Color_screen)


brett.main()
# screen = pygame.display.set_mode((width, height))


# s = Segment(300, 500, 100, screen)

# t = Tentacle(10, 500, screen)


# def main():

#     screen.fill(Color_screen)

#     while True:
#         mx, my = pygame.mouse.get_pos()

#         # t.follow(mx, my)
#         # # t.update()
#         # # t.draw()
#         # t.run()
#         s.follow(mx, my)
#         s.update()
#         s.draw()

#         # s.follow(mx, my)
#         # s.update()
#         # s.draw()
#         # print(str(s.x) + " " + str(s.y))

#         pygame.display.flip()
#         screen.fill(Color_screen)

#         for events in pygame.event.get():
#             if events.type == QUIT:

#                 sys.exit(0)


# main()
