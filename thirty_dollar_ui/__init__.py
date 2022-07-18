# -*- encoding: utf-8 -*-

"""
​

Don't you lecture me with your thirty dollar haircut
====================================================
The UI extension from the thirty dollar program
"""

import pygame
import thirty_dollar as td
import loader

loader.init(td.__database__)


class TDNoteUI(td.TDNote):
    def __init__(self, name: str or list):
        super().__init__(name)

