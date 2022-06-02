from app.http_client import HTTPClient
from app.misc.constants import ADDRESS_WEBSERVER, PORT_WEBSERVER
from app.ui.gui.objects.entry_list import EntryList
from app.ui.gui.windows.selected_service import WindowSelectedService


class FragmentServices:

    def __init__(self, root):
        http_client = HTTPClient(ADDRESS_WEBSERVER, PORT_WEBSERVER)
        list_of_services = http_client.get_list_services()

        entries = tuple(entry['id'] for entry in list_of_services)
        columns = tuple(['идентификатор'])

        EntryList(root, columns, entries, lambda tv: WindowSelectedService(root, entries[int(tv.selection()[0])]))
