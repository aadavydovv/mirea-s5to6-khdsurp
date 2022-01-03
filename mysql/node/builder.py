from mysql.base.builder_base import MySQLBuilderBase
from mysql.node.models import Job


class MySQLBuilderNode(MySQLBuilderBase):

    def add_job(self, service_id, job_metadata):
        return self._add_and_commit(Job(service_id=service_id, job_metadata=job_metadata))
