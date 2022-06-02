from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Node(Base):
    __tablename__ = 'node'

    host = Column(VARCHAR(16), primary_key=True)
    port = Column(INTEGER, nullable=False)
