import requests

from constants import ADDRESS_DB, PORT_DB, DB_USER, DB_PASSWORD, DB_NAME, ADDRESS_WEBSERVER
from mysql.db_jobs.client import MySQLClientJobs

if __name__ == '__main__':

    existing_services = requests.get(f'http://{ADDRESS_WEBSERVER}/list/services').json()
    with MySQLClientJobs(DB_USER,
                         DB_PASSWORD,
                         DB_NAME,
                         ADDRESS_DB,
                         PORT_DB,
                         db_exists=False) as mysql_client:
        try:
            mysql_client.initialize_database(tuple(service['id'] for service in existing_services))
        except Exception as e:
            print(f'jobs db init error: {e}')
