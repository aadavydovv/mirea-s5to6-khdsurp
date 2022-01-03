import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

from app.ui.gui.misc.constants import BG
from app.ui.gui.misc.functions import setup_widget_size


class WindowServiceDescription:
    class TextScrollCombo(ttk.Frame):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.grid_propagate(False)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

            self.txt = tk.Text(self)
            self.txt.grid(row=0, column=0, sticky=tk.NSEW, padx=2, pady=2)

            scrollbar = ttk.Scrollbar(self, command=self.txt.yview)
            scrollbar.grid(row=0, column=1, sticky='nsew')
            self.txt['yscrollcommand'] = scrollbar.set

    def __init__(self, root, text):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)
        setup_widget_size(self.widget, width_c=2.3, height_c=1.8)

        combo = self.TextScrollCombo(self.widget)
        combo.pack(fill=tk.BOTH, expand=True)
        combo.config(width=600, height=600)

        font = tkfont.Font(size=12)
        combo.txt.config(font=font, undo=True, wrap='word')
        combo.txt.config(borderwidth=3, relief=tk.SUNKEN)

        combo.txt.insert(tk.INSERT, text)
        combo.txt.configure(state='disabled')
