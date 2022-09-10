# -*- encoding: utf-8 -*-

import pygame


class ProgressBar:
    def __init__(self, x: float, y: float, width: float, height: float, steps: int, surface: pygame.surface.Surface,
                 color, background_color):
        self.surface = surface

        self.rect = pygame.rect.Rect(x, y, width, height)
        self.fill_rect = pygame.rect.Rect(x, y, 0, height)
        self.pos = (x, y)

        self.color = color
        self.bg_color = background_color

        self.steps = steps
        self.c_step = 0

        self.width = width
        self.height = height

        self.size = width

    def update(self):
        pygame.draw.rect(self.surface, self.bg_color, self.rect)
        pygame.draw.rect(self.surface, self.color, self.fill_rect)
        pygame.display.update(self.rect)

    def increment(self):
        self.c_step += 1
        if self.c_step > self.steps:
            self.c_step = self.steps

    def calculate(self):
        self.size = self.c_step / self.steps
        self.size = self.size * self.width

        self.fill_rect.update(self.pos, (self.size, self.height))
    
    def step(self):
        self.increment()
        self.calculate()
        self.update()


class Text:
    def __init__(self, x: float, y: float, font: pygame.font.Font or str, surface: pygame.Surface, size: int = None):
        if isinstance(font, str):
            assert size, "No size given"
            self.font = pygame.font.Font(font, size)
        elif isinstance(font, pygame.font.Font):
            self.font = font
        else:
            raise ValueError(f"Needed a font or an access path, got {type(font)} instead")

        self.pos = (x, y)
        self.surface = surface

        self.height = self.font.size("a")[1]

    def render(self, text: str, color: tuple, antialias: bool = False):
        text_lines = text.splitlines()
        _r = []
        for line in text_lines:
            _r.append(self.font.render(line, antialias, color))

        i = 0
        for r in _r:
            self.surface.blit(r, (self.pos[0], self.pos[1] + (i * self.height)))
            i += 1

        del _r
