#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Thitry Dollar Midi UI.

TTK schemes.
"""
import tkinter as tk

widget: tk.ttk = tk.ttk

style: widget.Style = widget.Style()
style.theme_create("light", settings={
    "TFrame": {
        ""
    }
})