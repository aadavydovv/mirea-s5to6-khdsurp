from mysql.base.client_base import MySQLClientBase
from mysql.db_services.builder import MySQLBuilderServices
from mysql.db_services.constants import DB_NAME
from mysql.db_services.models import Service


class MySQLClientServices(MySQLClientBase):

    def __init__(self, user, password, db_name, host, port, db_exists=True):
        super().__init__(user, password, db_name, host, port, MySQLBuilderServices, db_exists)

    def get_services(self, are_keys_needed=False):
        query = self.session.query(Service)
        if are_keys_needed:
            to_return = query.all(), Service.__table__.columns
        else:
            to_return = query.all()
        return to_return

    def get_service(self, service_id):
        return self.session.query(Service).get(service_id)

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

        for n in range(1, 11):
            service_id = f'service_{str(n).zfill(2)}'
            self.add_service(service_id, f'описание службы "{service_id}"')
