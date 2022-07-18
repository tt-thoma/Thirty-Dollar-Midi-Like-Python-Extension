# -*- encoding: utf-8 -*-

import pygame
import os


# DATA PATHS
#
# Images: data / images / type / id
# Sounds: data / audio / id
#
# REAL PATHS
#
# Images: ./data/assets/sound/id.png
# Sounds: ./data/audio/id.wav
# Fonts: ./data/fonts


def init(data: dict):
    # Preparing up the terrain
    data["data"] = {}
    data["data"]["images"] = {}
    data["data"]["audio"] = {}

    print("Loading assets...")

    i = 2
    for t in ["action", "sound"]:
        for a in data["id"][t]:
            data["data"]["images"][t][a] = pygame.image.load(f"data/assets/{t}/{a}.png")
            i += 1
    data["data"]["images"]["pause"] = [pygame.image.load("data/assets/empty.png")]
    print(f"Loaded {i} assets.")

    print("Loading sounds...")
    i = 1
    for s in data["id"]["sound"]:
        data["data"]["audio"][s] = pygame.sound.load(f"data/audio/{s}.wav")
        i += 1

    print(f"Loaded {i} sounds.")
