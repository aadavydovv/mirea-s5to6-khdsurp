import tkinter as tk
import tkinter.font as tkfont

from app.ui.gui.misc.constants import FG, BUTTON_BG, LEFT_MOUSE_BUTTON


class Button(tk.Button):

    def __init__(self, text, master, action=None, font_size=12):
        font = tkfont.Font(size=font_size)

        super().__init__(master, text=text, fg=FG, bg=BUTTON_BG, highlightthickness=0, bd=0, font=font)

        if action:
            self.bind(LEFT_MOUSE_BUTTON, action)
