import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

from app.ui.gui.misc.constants import FG, BG


class Label(ttk.Label):

    def __init__(self, text, master, font_size=18, anchor=tk.CENTER, fg=FG, bg=BG):
        font = tkfont.Font(size=font_size)
        super().__init__(master, text=text, foreground=fg, background=bg, font=font, anchor=anchor, justify=tk. CENTER)
