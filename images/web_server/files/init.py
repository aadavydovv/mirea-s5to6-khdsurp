from sqlalchemy.exc import ProgrammingError

from constants import DB_NODES_USER, DB_NODES_PASSWORD, DB_NODES_NAME, DB_SERVER_ADDRESS, DB_SERVER_PORT, \
    LIST_OF_NODES, DB_SERVICES_USER, DB_SERVICES_PASSWORD, DB_SERVICES_NAME
from mysql.db_nodes.client import MySQLClientNodes
from mysql.db_services.client import MySQLClientServices


def main():
    with MySQLClientNodes(DB_NODES_USER,
                          DB_NODES_PASSWORD,
                          DB_NODES_NAME,
                          DB_SERVER_ADDRESS,
                          DB_SERVER_PORT, db_exists=False) as mysql_nodes_db_client:
        try:
            mysql_nodes_db_client.initialize_database(LIST_OF_NODES)
        except ProgrammingError as e:
            print(e)  # TODO: bruh

    with MySQLClientServices(DB_SERVICES_USER,
                             DB_SERVICES_PASSWORD,
                             DB_SERVICES_NAME,
                             DB_SERVER_ADDRESS,
                             DB_SERVER_PORT,
                             db_exists=False) as mysql_services_db_client:
        try:
            mysql_services_db_client.initialize_database()
        except ProgrammingError as e:
            print(e)  # TODO: bruh


if __name__ == '__main__':
    main()
