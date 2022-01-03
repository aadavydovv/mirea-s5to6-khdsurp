import random

from mysql.base.client_base import MySQLClientBase
from mysql.node.builder import MySQLBuilderNode
from mysql.node.constants import DB_NAME
from mysql.node.models import Job


class MySQLClientNode(MySQLClientBase):

    def __init__(self, user, password, db_name, host, port, db_exists=True):
        super().__init__(user, password, db_name, host, port, MySQLBuilderNode, db_exists)

    def add_job(self, service_id, node_id):
        return self._builder.add_job(service_id, node_id)

    def get_job_by_service_id(self, service_id):
        return self.session.query(Job).filter(Job.service_id == service_id).first()

    # temporary
    def initialize_database(self, list_of_service_ids):
        self._connection.execute(f'CREATE DATABASE {DB_NAME}')

        self._connection.close()
        self._db_exists = True
        self._db_name = DB_NAME
        self._connect()

        Job.metadata.tables[Job.__tablename__].create(self._engine)

        for service_id in random.sample(list_of_service_ids, len(list_of_service_ids) // random.choice((2, 3, 4))):
            self.add_job(service_id, f'метаданные работы сервиса "{service_id}"')
