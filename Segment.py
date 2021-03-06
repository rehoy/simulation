import sys
import pygame
from math import atan2, sqrt
from pygame.locals import*
from math import sin, cos, atan2, degrees


class Segment:
    def __init__(self, x, y, len, screen):
        self.x = x
        self.y = y
        self.vinkel = 0
        self.len = len
        self.bx, self.by = 200, 200
        self.screen = screen
        self.color = (255, 0, 0)
        self.cosinus = 0

    def draw(self):
        pygame.draw.line(self.screen, self.color,
                         (self.x, self.y), (self.bx, self.by))

    def calculateEnd(self):

        dx = self.len * cos(self.vinkel)
        dy = self.len * sin(self.vinkel)

        self.bx = self.x + dx
        self.by = self.y + dy

    def follow(self, tx, ty):

        self.vinkel = atan2(ty - self.y, tx - self.x)

        self.x = tx
        self.y = ty

        self.bx = self.x - (self.len * cos(self.vinkel))
        self.by = self.y - (self.len * sin(self.vinkel))

        self.bx, self.x = self.x, self.bx
        self.by, self.y = self.y, self.by

        # if tx > self.x:

        #     self.x = self.x + (tx - self.x) - (self.len * cos(self.vinkel))
        #     self.bx = tx + (tx - self.bx) - (self.len * cos(self.vinkel))
        # else:
        #     self.x = self.x - (self.x - tx) + (self.len * cos(self.vinkel))
        #     self.bx = self.bx - (self.bx - tx) + (self.len * cos(self.vinkel))

        # if tx > self.y:

        #     self.y = self.y + (ty - self.y) - (self.len * sin(self.vinkel))
        #     self.by = ty + (tx - self.by) - (self.len * sin(self.vinkel))
        # else:

        #     self.y = self.y - (self.y - ty) + (self.len * sin(self.vinkel))
        #     self.by = self.by - (self.by - ty) + (self.len * sin(self.vinkel))

    def update(self):
        self.calculateEnd()

    def move(self):
        dx = cos(self.vinkel)
        dy = sin(self.vinkel)

        self.x += dx
        self.y += dy

    def seek(self, tx, ty):
        v2x = 0
        v2y = 0

        if tx > self.x:
            v2x = tx - self.x
        else:
            v2x = self.x - tx

        if ty > self.y:
            v2y = ty - self.y
        else:
            v2y = self.y - ty

        vx = self.len * cos(self.vinkel)
        vy = self.len * sin(self.vinkel)

        top = (v2x * vx) + (v2y * vy)
        bot = self.len * sqrt(v2x * v2x + v2y * v2y)
        cosinus = top / bot

        if (cosinus != self.cosinus):
            print(cosinus)
        self.cosinus = cosinus

        return v2x, v2y

    def move():
        pass
