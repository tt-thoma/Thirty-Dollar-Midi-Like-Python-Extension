# -*- encoding: utf-8 -*-

import pygame


class ProgressBar:
    def __init__(self, x: float, y: float, width: float, height: float, steps: int, surface: pygame.surface.Surface, color):
        self.surface = surface

        self.rect = pygame.rect.Rect(x, y, x + width, y + height)
        self.pos = (x, y)

        self.color = color

        self.steps = steps
        self.step = 0

        self.width = width
        self.height = height

        self.size = width

    def update(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
        pygame.display.update(self.rect)

    def increment(self):
        self.step += 1
        if self.step > self.steps:
            self.step = self.steps

        self.size = self.step / self.steps
        self.size = self.size * self.width
