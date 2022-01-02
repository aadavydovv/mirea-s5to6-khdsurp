from sqlalchemy.exc import ProgrammingError

from http_client import HTTPClient
from misc.constants import (LIST_OF_NODES, DB_SERVICES_PORT, DB_SERVICES_NAME, DB_SERVICES_HOST, DB_SERVICES_USER,
                            DB_SERVICES_PASSWORD, DB_NODES_NAME, DB_NODES_PORT, DB_NODES_PASSWORD, DB_NODES_HOST,
                            DB_NODES_USER)
from mysql.nodes_db.client import MySQLClientNodesDB
from mysql.services_db.client import MySQLClientServicesDB


def init_nodes_db():
    with MySQLClientNodesDB(DB_NODES_USER,
                            DB_NODES_PASSWORD,
                            DB_NODES_NAME,
                            DB_NODES_HOST,
                            DB_NODES_PORT, db_exists=False) as mysql_nodes_db_client:
        try:
            mysql_nodes_db_client.initialize_database(LIST_OF_NODES)
        except ProgrammingError:
            pass


if __name__ == '__main__':
    init_nodes_db()

    with MySQLClientServicesDB(DB_SERVICES_USER,
                               DB_SERVICES_PASSWORD,
                               DB_SERVICES_NAME,
                               DB_SERVICES_HOST,
                               DB_SERVICES_PORT) as mysql_services_db_client:
        services = mysql_services_db_client.get_services()

    print('список служб:')
    for n in range(len(services)):
        print(f'\t{n + 1}) {services[n].id}')

    selected_service_number = int(input('\n'
                                        'введите номер службы: ')) - 1
    selected_service = services[selected_service_number]
    print(f'вы выбрали службу {selected_service.id}')

    with MySQLClientNodesDB(DB_NODES_USER, DB_NODES_PASSWORD, DB_NODES_NAME, DB_NODES_HOST,
                            DB_NODES_PORT) as mysql_nodes_db_client:
        list_of_nodes = mysql_nodes_db_client.get_nodes()

    for node in list_of_nodes:
        http_client = HTTPClient(node.host, node.port)
        status_service = http_client.get_status_service(selected_service.id)
        print(f'for host {node.host}: {status_service.get("message")}')

    print()

    for node in list_of_nodes:
        http_client = HTTPClient(node.host, node.port)
        status_upgrade = http_client.get_status_upgrade()

        if status_upgrade.get('message') == '0':
            message_modifier = ' not '
        else:
            message_modifier = ' '

        print(f'for host {node.host}: upgrade is{message_modifier}needed')
