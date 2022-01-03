import tkinter as tk

from ui.gui.misc.constants import BG, PAD_X, PAD_Y
from ui.gui.misc.functions import setup_widget_size, pack_default
from ui.gui.objects.entry_list import EntryList


class WindowResultEntryList:

    def __init__(self, root, columns, entries):
        self.widget = tk.Toplevel(root, bg=BG, padx=PAD_X, pady=PAD_Y)
        setup_widget_size(self.widget, resizable=True, maxsize=True)

        print(columns, entries)
        EntryList(self.widget, columns, entries, None, selectmode=tk.NONE)
