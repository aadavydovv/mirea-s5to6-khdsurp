import tkinter as tk

from app.http_client import HTTPClient
from app.misc.constants import ADDRESS_WEBSERVER, PORT_WEBSERVER
from app.ui.gui.objects.entry_list import EntryList
from mysql.db_nodes.client import MySQLClientNodes


class FragmentNodes:

    def __init__(self, root):
        http_client = HTTPClient(ADDRESS_WEBSERVER, PORT_WEBSERVER)
        list_of_nodes = http_client.get_list_nodes()

        list_of_statuses = []

        for node in list_of_nodes:
            status_upgrade = http_client.get_status_update(node['host'])

            message = 'обновление не требуется' if status_upgrade == 0 else 'требуется обновление'
            list_of_statuses.append(message)

        columns = 'адрес', 'статус'
        entries = list(zip([node['host'] for node in list_of_nodes], list_of_statuses))

        EntryList(root, columns, entries, None, selectmode=tk.NONE)
