import random

from mysql.base.client_base import MySQLClientBase
from mysql.db_jobs.builder import MySQLBuilderJobs
from mysql.db_jobs.constants import DB_NAME
from mysql.db_jobs.models import Job


class MySQLClientJobs(MySQLClientBase):

    def __init__(self, user, password, db_name, host, port, db_exists=True):
        super().__init__(user, password, db_name, host, port, MySQLBuilderJobs, db_exists)

    def add_job(self, service_id, job_metadata):
        return self._builder.add_job(service_id, job_metadata)

    def get_job_by_service_id(self, service_id):
        return self.session.query(Job).filter(Job.id_service == service_id).first()

    def get_job_description(self, job_id):
        return self.session.query(Job).get(job_id).job_metadata

    # temporary
    def initialize_database(self, list_of_service_ids):
        self._connection.execute(f'CREATE DATABASE {DB_NAME}')

        self._connection.close()
        self._db_exists = True
        self._db_name = DB_NAME
        self._connect()

        Job.metadata.tables[Job.__tablename__].create(self._engine)

        for service_id in random.sample(list_of_service_ids, len(list_of_service_ids) // random.choice((2, 3, 4))):
            self.add_job(service_id, f'метаданные работы службы "{service_id}"')
