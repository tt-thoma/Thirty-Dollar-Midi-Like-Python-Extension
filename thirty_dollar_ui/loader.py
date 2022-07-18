# -*- encoding: utf-8 -*-

import pygame
import os


# DATA PATHS
#
# Images:
#


def init(data: dict):
    # Preparing up the terrain
    data["data"] = {}
    data["data"]["images"] = {}

    print("Loading images...")
    data["data"]["images"]["pause"] = [pygame.image.load("")]
