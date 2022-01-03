import tkinter as tk
from tkinter import ttk

from app.http_client import HTTPClient
from app.misc.constants import (DB_NODES_USER, DB_NODES_PASSWORD, DB_NODES_NAME, DB_NODES_HOST, DB_NODES_PORT,
                                DB_SERVICES_USER, DB_SERVICES_PASSWORD, DB_SERVICES_NAME, DB_SERVICES_HOST,
                                DB_SERVICES_PORT)
from mysql.nodes_db.client import MySQLClientNodesDB
from mysql.services_db.client import MySQLClientServicesDB
from app.ui.gui.misc.constants import BG, PAD_X, PAD_Y
from app.ui.gui.misc.functions import setup_widget_size
from app.ui.gui.objects.button import Button
from app.ui.gui.objects.entry_list import EntryList
from app.ui.gui.objects.label import Label
from app.ui.gui.windows.service_description import WindowServiceDescription


class WindowSelectedService:

    def __init__(self, root, service_id):
        self.widget = tk.Toplevel(root, bg=BG, padx=PAD_X, pady=PAD_Y)
        setup_widget_size(self.widget, resizable=False, width_c=2.5, height_c=1.5)

        Label(f'служба "{service_id}"', self.widget).pack(pady=(0, 16))

        with MySQLClientNodesDB(DB_NODES_USER, DB_NODES_PASSWORD, DB_NODES_NAME, DB_NODES_HOST,
                                DB_NODES_PORT) as mysql_nodes_db_client:
            list_of_nodes = mysql_nodes_db_client.get_nodes()

        list_of_status_messages = []

        for node in list_of_nodes:
            http_client = HTTPClient(node.host, node.port)

            service_status_data = http_client.get_status_service(service_id).get('message')
            if service_status_data['service_status'] == 1:
                list_of_status_messages.append(f'активна, ID работы: {service_status_data["job_id"]}')
            else:
                list_of_status_messages.append('неактивна')

        columns = 'адрес узла', 'статус'
        entries = list(zip([node.host for node in list_of_nodes], list_of_status_messages))

        frame_tv = ttk.Frame(self.widget)
        EntryList(frame_tv, columns, entries, None, selectmode=tk.NONE)

        def on_click_button_description():
            with MySQLClientServicesDB(DB_SERVICES_USER, DB_SERVICES_PASSWORD, DB_SERVICES_NAME, DB_SERVICES_HOST,
                                       DB_SERVICES_PORT) as mysql_services_db_client:
                description = mysql_services_db_client.get_service(service_id).description
            WindowServiceDescription(self.widget, description)

        Button('показать описание', self.widget,
               action=lambda event: on_click_button_description()) \
            .pack(fill=tk.X, ipadx=PAD_X, ipady=PAD_Y, side=tk.BOTTOM, pady=(16, 0))

        frame_tv.pack(fill=tk.BOTH)
