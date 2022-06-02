import tkinter as tk
from tkinter import ttk

from app.http_client import HTTPClient
from app.misc.constants import ADDRESS_WEBSERVER, PORT_WEBSERVER
from app.ui.gui.misc.constants import BG, PAD_X, PAD_Y
from app.ui.gui.misc.functions import setup_widget_size
from app.ui.gui.objects.button import Button
from app.ui.gui.objects.entry_list import EntryList
from app.ui.gui.objects.label import Label
from app.ui.gui.windows.description import WindowDescription


class WindowSelectedService:

    def __init__(self, root, service_id):
        self.widget = tk.Toplevel(root, bg=BG, padx=PAD_X, pady=PAD_Y)
        setup_widget_size(self.widget, resizable=False, width_c=2.5, height_c=1.5)

        Label(f'служба "{service_id}"', self.widget).pack(pady=(0, 16))

        self.http_client = HTTPClient(ADDRESS_WEBSERVER, PORT_WEBSERVER)

        list_of_nodes = self.http_client.get_list_nodes()

        list_of_status_messages = []

        for node in list_of_nodes:
            service_status_data = self.http_client.get_status_service(node['host'], service_id)
            if service_status_data['service_status'] == 1:
                list_of_status_messages.append(f'активна, ID работы: {service_status_data["job_id"]}')
            else:
                list_of_status_messages.append('неактивна')

        columns = 'адрес узла', 'статус'
        entries = list(zip([node['host'] for node in list_of_nodes], list_of_status_messages))

        frame_tv = ttk.Frame(self.widget)

        def make_job_description(tv):
            selected_entry = entries[int(tv.selection()[0])]
            node_address = selected_entry[0]
            job_id = selected_entry[1].partition(': ')[2]

            job_description = self.http_client.get_description_job(node_address, job_id)
            WindowDescription(self.widget, job_description)

        EntryList(frame_tv, columns, entries, lambda tv: make_job_description(tv))

        def on_click_button_description():
            description = self.http_client.get_description_service(service_id)
            WindowDescription(self.widget, description)

        Button('показать описание', self.widget,
               action=lambda event: on_click_button_description()) \
            .pack(fill=tk.X, ipadx=PAD_X, ipady=PAD_Y, side=tk.BOTTOM, pady=(16, 0))

        frame_tv.pack(fill=tk.BOTH)
