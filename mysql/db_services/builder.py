from mysql.base.builder_base import MySQLBuilderBase
from mysql.db_services.models import Service


class MySQLBuilderServices(MySQLBuilderBase):

    def add_service(self, service_id, description):
        return self._add_and_commit(Service(id=service_id, description=description))
