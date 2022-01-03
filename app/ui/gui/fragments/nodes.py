import tkinter as tk

from app.http_client import HTTPClient
from app.misc.constants import DB_NODES_USER, DB_NODES_PASSWORD, DB_NODES_NAME, DB_NODES_HOST, DB_NODES_PORT
from app.ui.gui.objects.entry_list import EntryList
from mysql.nodes_db.client import MySQLClientNodesDB


class FragmentNodes:

    def __init__(self, root):
        with MySQLClientNodesDB(DB_NODES_USER, DB_NODES_PASSWORD, DB_NODES_NAME, DB_NODES_HOST,
                                DB_NODES_PORT) as mysql_nodes_db_client:
            list_of_nodes = mysql_nodes_db_client.get_nodes()

        list_of_statuses = []

        for node in list_of_nodes:
            http_client = HTTPClient(node.host, node.port)
            status_upgrade = http_client.get_status_upgrade()

            message = 'обновление не требуется' if status_upgrade.get('message') == 0 else 'требуется обновление'
            list_of_statuses.append(message)

        columns = 'адрес', 'статус'
        entries = list(zip([node.host for node in list_of_nodes], list_of_statuses))

        EntryList(root, columns, entries, None, selectmode=tk.NONE)
