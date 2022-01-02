from mysql.services_db.models import Service
from mysql.services_db.constants import DB_NAME
from mysql.base.client_base import MySQLClientBase
from mysql.services_db.builder import MySQLBuilderServicesDB


class MySQLClientServicesDB(MySQLClientBase):

    def __init__(self, user, password, db_name, host, port, db_exists=True):
        super().__init__(user, password, db_name, host, port, MySQLBuilderServicesDB, db_exists)

    def get_services(self):
        return self.session.query(Service).all()

    # temporary
    def add_service(self, service_id, service_description):
        return self._builder.add_service(service_id, service_description)

    # temporary
    def initialize_database(self):
        self._connection.execute(f'CREATE DATABASE {DB_NAME}')

        self._connection.close()
        self._db_exists = True
        self._db_name = DB_NAME
        self._connect()

        Service.metadata.tables[Service.__tablename__].create(self._engine)

        self.add_service('service_01', 'description of service_01')
        self.add_service('service_02', 'description of service_02')
        self.add_service('service_03', 'description of service_03')
        self.add_service('service_04', 'description of service_04')
        self.add_service('service_06', 'description of service_06')
        self.add_service('service_07', 'description of service_07')
        self.add_service('service_08', 'description of service_08')
        self.add_service('service_09', 'description of service_09')
        self.add_service('service_10', 'description of service_10')
