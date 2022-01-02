from sqlalchemy.exc import ProgrammingError

from constants import (DB_SERVICES_PORT, DB_SERVICES_USER, DB_SERVICES_PASSWORD, DB_SERVICES_NAME, DB_SERVICES_HOST,
                       DB_NODE_PASSWORD, DB_NODE_NAME, DB_NODE_HOST, DB_NODE_PORT, DB_NODE_USER)
from mysql.node.client import MySQLClientNode
from mysql.services_db.client import MySQLClientServicesDB

if __name__ == '__main__':

    with MySQLClientServicesDB(DB_SERVICES_USER,
                               DB_SERVICES_PASSWORD,
                               DB_SERVICES_NAME,
                               DB_SERVICES_HOST,
                               DB_SERVICES_PORT,
                               db_exists=False) as mysql_services_db_client:
        try:
            mysql_services_db_client.initialize_database()
        except ProgrammingError:
            pass

    with MySQLClientServicesDB(DB_SERVICES_USER,
                               DB_SERVICES_PASSWORD,
                               DB_SERVICES_NAME,
                               DB_SERVICES_HOST,
                               DB_SERVICES_PORT) as mysql_services_db_client:
        existing_services = mysql_services_db_client.get_services()

    with MySQLClientNode(DB_NODE_USER,
                         DB_NODE_PASSWORD,
                         DB_NODE_NAME,
                         DB_NODE_HOST,
                         DB_NODE_PORT,
                         db_exists=False) as mysql_client:
        mysql_client.initialize_database(tuple(service.id for service in existing_services))
