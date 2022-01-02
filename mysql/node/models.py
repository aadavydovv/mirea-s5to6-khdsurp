from sqlalchemy import VARCHAR, Column, INTEGER
from sqlalchemy.ext.declarative import declarative_base

from mysql.node.constants import SERVICE_ID_LENGTH

Base = declarative_base()


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    service_id = Column(VARCHAR(SERVICE_ID_LENGTH), nullable=False)
    job_metadata = Column(VARCHAR(512), nullable=False)  # пока условно
