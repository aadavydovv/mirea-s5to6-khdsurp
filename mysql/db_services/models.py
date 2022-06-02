from sqlalchemy import VARCHAR, Column
from sqlalchemy.ext.declarative import declarative_base

from mysql.db_services.constants import SERVICE_DESCRIPTION_LENGTH, SERVICE_ID_LENGTH

Base = declarative_base()


class Service(Base):
    __tablename__ = 'service'

    id = Column(VARCHAR(SERVICE_ID_LENGTH), primary_key=True)
    description = Column(VARCHAR(SERVICE_DESCRIPTION_LENGTH), nullable=True)
