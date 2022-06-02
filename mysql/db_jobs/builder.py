from mysql.base.builder_base import MySQLBuilderBase
from mysql.db_jobs.models import Job


class MySQLBuilderJobs(MySQLBuilderBase):

    def add_job(self, service_id, job_metadata):
        return self._add_and_commit(Job(id_service=service_id, job_metadata=job_metadata))
