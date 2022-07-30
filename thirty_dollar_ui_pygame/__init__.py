# -*- encoding: utf-8 -*-

"""
​

Don't you lecture me with your thirty dollar haircut
====================================================
The UI extension from the thirty dollar program
"""

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


import pygame
import thirty_dollar as td
from . import loader

loader.init(td.__database__)


class TDNoteUI(td.TDNote):
    def __init__(self, data: str or list or td.TDNote):
        if isinstance(data, td.TDNote) and data:
            # Duplicate the data from a class to another
            #
            # __dict__: Variables
            # dir(): Functions

            for i in data.__dict__:
                self.__dict__[i] = data.__dict__[i]

            for i in dir(data):
                if not i.startswith("__"):
                    setattr(self, i, getattr(data, i))
        else:
            # Initialize normally
            super().__init__(data)

        # Load the image
        self.image = td.__database__["data"]["image"][self.type][self.id]
        self.rect = self.image.get_rect()

        # Load the sound
        if self.type == "sound":
            self.sound = td.__database__["data"]["audio"][self.id]


class TDFileUI(td.TDFile):
    def __init__(self, data: str or list):
        super().__init__(data)
        for i in range(len(self.sequence) - 1):
            # print(f"Converting... {i + 1}/{len(self.sequence) - 1}")
            self.sequence[i] = TDNoteUI(self.sequence[i])


f = TDFileUI("sample/Big Shot (DELTARUNE)")
