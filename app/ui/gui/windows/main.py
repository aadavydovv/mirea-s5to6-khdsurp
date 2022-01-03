import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

from app.ui.gui.fragments.nodes import FragmentNodes
from app.ui.gui.fragments.services import FragmentServices
from app.ui.gui.misc.constants import BG
from app.ui.gui.misc.functions import setup_widget_size


class WindowMain:

    def __init__(self):
        def _configure_style():
            style = ttk.Style(self.widget)

            style.configure('TNotebook.Tab', width=self.widget.winfo_screenwidth())
            style.configure('TNotebook.Tab', padding=16)
            font = tkfont.Font(size=16)  # this number means nothing, not sure what's going on
            style.configure('TNotebook.Tab', font=font)

            style.configure('Treeview', rowheight=48, padding=4)

            style.configure("Custom.Treeview.Heading", padding=4)

            # hide dotted line when selecting tabs
            style.layout('Tab', [('Notebook.tab',
                                  {'sticky': 'nswe',
                                   'children': [('Notebook.padding',
                                                 {'side': 'top', 'sticky': 'nswe',
                                                  'children': [('Notebook.label',
                                                                {'side': 'top',
                                                                 'sticky': ''})], })], })])

        self.widget = tk.Tk()
        self.widget.configure(bg=BG, padx=16, pady=16)
        setup_widget_size(self.widget, maxsize=True, width_c=2.8, height_c=1.3)

        _configure_style()

        notebook = ttk.Notebook(self.widget)
        notebook.pack(expand=True, fill='both')

        frame_services = ttk.Frame(notebook)
        frame_nodes = ttk.Frame(notebook)

        frame_services.pack(fill='both', expand=True)
        frame_nodes.pack(fill='both', expand=True)

        notebook.add(frame_services, text='службы')
        notebook.add(frame_nodes, text='узлы')

        FragmentServices(frame_services)
        FragmentNodes(frame_nodes)
