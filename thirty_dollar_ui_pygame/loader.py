# -*- encoding: utf-8 -*-

import pygame
pygame.mixer.pre_init()
pygame.mixer.init()

# DATA PATHS
#
# Images: data / image / type / id
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
    data["data"]["image"] = {}
    data["data"]["image"]["action"] = []
    data["data"]["image"]["sound"] = []
    data["data"]["audio"] = []

    print("Loading assets...")

    i = 2
    for t in ["action", "sound"]:
        for a in data["id"][t]:
            data["data"]["image"][t].append(pygame.image.load(f"data/assets/{t}/{a}.png"))
            # print(f"Loaded {a}.png")
            i += 1
    data["data"]["image"]["pause"] = [pygame.image.load("data/assets/empty.png")]

    print("Loading sounds...")
    i = 1
    for s in data["id"]["sound"]:
        data["data"]["audio"].append(pygame.mixer.Sound(f"data/audio/{s}.wav"))
        # print(f"Loaded {s}.wav")
        i += 1

    print("Done.\n")
