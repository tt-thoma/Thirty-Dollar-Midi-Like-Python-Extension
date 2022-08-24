# -*- encoding: utf-8 -*-

import pygame

from time import sleep
from . import elements
from . import loader


def init(data, config):
    pygame.init()

    width = config["window"]["width"]
    height = config["window"]["height"]

    screen = pygame.display.set_mode((width, height))

    icon = pygame.image.load("data/assets/sound/boom.png")
    pygame.display.set_caption("Loading...")
    pygame.display.set_icon(icon)

    count = len(data["id"]["sound"]) * 2
    count += len(data["id"]["action"])

    screen.fill((48, 42, 74))
    bar = elements.ProgressBar(20, 20, width - 40, 20, count, screen, (243, 236, 37), (90, 90, 90))
    bar.update()

    pygame.display.flip()

    while True:
        bar.step()
        sleep(0.1)

    sleep(5)

    loader.init(data, bar.step)

    sleep(5)
