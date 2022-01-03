from app.misc.constants import DB_SERVICES_PORT, DB_SERVICES_HOST, DB_SERVICES_NAME, DB_SERVICES_USER, DB_SERVICES_PASSWORD
from mysql.services_db.client import MySQLClientServicesDB
from app.ui.gui.objects.entry_list import EntryList
from app.ui.gui.windows.selected_service import WindowSelectedService


class FragmentServices:

    def __init__(self, root):
        with MySQLClientServicesDB(DB_SERVICES_USER, DB_SERVICES_PASSWORD, DB_SERVICES_NAME, DB_SERVICES_HOST,
                                   DB_SERVICES_PORT) as mysql_client:
            db_data = mysql_client.get_services(are_keys_needed=True)
            entries = tuple(entry.id for entry in db_data[0])
            columns = tuple(['идентификатор'])

        EntryList(root, columns, entries, lambda tv: WindowSelectedService(root, entries[int(tv.selection()[0])]))
