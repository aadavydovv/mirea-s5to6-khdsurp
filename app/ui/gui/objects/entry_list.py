import tkinter
import tkinter as tk
from tkinter import ttk

from app.ui.gui.misc.constants import BG


class EntryList:

    def __init__(self, root, columns, entries, action_on_select, selectmode=tk.BROWSE):
        self.tv = ttk.Treeview(root, selectmode=selectmode, style='Custom.Treeview')

        self.tv['columns'] = columns

        self.tv.column('#0', width=0, stretch=tkinter.NO)

        for column in columns:
            self.tv.column(column, anchor=tkinter.W)
            self.tv.heading(column, text=column, anchor=tkinter.W)

        for n in range(len(entries)):
            self.tv.insert(parent='', index=n, iid=n, text='', values=entries[n])

        if not selectmode == tk.NONE:
            def modified_action_on_select():
                # remove other spawned service action windows if such exist
                frame_children = root.winfo_children()
                if len(frame_children) > 2:
                    for child in frame_children[3:]:
                        child.destroy()

                action_on_select(self.tv)

            self.tv.bind('<Double-1>', lambda event: modified_action_on_select())

        frame_buttons = tk.Frame(root, relief=tk.RAISED, background=BG)
        frame_buttons.pack(side=tkinter.RIGHT)

        scroll_v = ttk.Scrollbar(root, orient='vertical', command=self.tv.yview)
        scroll_v.pack(fill=tkinter.Y, side=tkinter.RIGHT)

        self.tv.pack(fill=tkinter.BOTH, expand=True)

        self.tv.configure(yscrollcommand=scroll_v.set)
