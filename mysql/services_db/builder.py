from mysql.base.builder_base import MySQLBuilderBase
from mysql.services_db.models import Service


class MySQLBuilderServicesDB(MySQLBuilderBase):

    def add_service(self, service_id, service_description):
        return self._add_and_commit(Service(id=service_id, description=service_description))
