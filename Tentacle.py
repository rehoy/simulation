from Segment import Segment
import pygame
from pygame.locals import*


class Tentacle:

    def __init__(self, segments, len, screen):
        self.ant_segments = segments
        self.len = len
        self.seg_len = round(self.len / self.ant_segments)
        self.segments = []
        self.screen = screen
        self.color = (255, 255, 255)

        self._make_tentacle()

    def _make_tentacle(self):

        for i in range(self.ant_segments):
            s = Segment(100, 100, self.seg_len, self.screen)
            self.segments.append(s)

    def follow(self, tx, ty):
        self.segments[0].follow(tx, ty)

        for i in range(1, self.ant_segments):
            self.segments[i].follow(self.segments[i-1].x, self.segments[i-1].y)

    def update(self):
        for i in self.segments:
            i.update()

    def draw(self):
        for i in self.segments:
            pygame.draw.line(self.screen, self.color,
                             (i.x, i.y), (i.bx, i.by), 200)

    def run(self):
        for i in self.segments:
            # i.update()
            pygame.draw.line(self.screen, self.color,
                             (i.x, i.y), (i.bx, i.by))
