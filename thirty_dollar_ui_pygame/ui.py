# -*- encoding: utf-8 -*-

import pygame
import traceback
import sys

from time import sleep
from . import elements
from . import loader


def init(data, config):
    pygame.init()

    clock = pygame.time.Clock()
    fps = config["FPS"]

    width = config["window"]["width"]
    height = config["window"]["height"]

    icon = pygame.image.load("data/assets/sound/boom.png")
    pygame.display.set_caption("Loading...")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((width, height))

    text = pygame.font.Font("data/fonts/ubuntu.ttf", 24)
    info = elements.Text(20, 20, text, screen)

    count = len(data["id"]["sound"]) * 2
    count += len(data["id"]["action"])

    screen.fill((48, 42, 74))

    info.render(f"Loading {count} assets", (255, 255, 255), True)
    bar = elements.ProgressBar(20, height - 50, width - 40, 20, count, screen, (243, 236, 37), (90, 90, 90))
    bar.update()

    pygame.display.flip()

    try:
        loader.init(data, bar.step)
    except:
        info.render(str(traceback.format_exc()), (203, 36, 33), True)
        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    break
        raise

    del bar, info
    title = elements.Text(20, 20, "data/fonts/ubuntu-bold.ttf", screen, 42)

    while True:
        screen.fill((48, 42, 74))
        title.render("Welcome Aboard!", (255, 255, 255), True)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(fps)
