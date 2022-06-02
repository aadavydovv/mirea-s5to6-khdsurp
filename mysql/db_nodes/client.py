from mysql.base.client_base import MySQLClientBase
from mysql.db_nodes.builder import MySQLBuilderNodes
from mysql.db_nodes.constants import DB_NAME
from mysql.db_nodes.models import Node


class MySQLClientNodes(MySQLClientBase):

    def __init__(self, user, password, db_name, host, port, db_exists=True):
        super().__init__(user, password, db_name, host, port, MySQLBuilderNodes, db_exists)

    def get_nodes(self):
        return self.session.query(Node).all()

    def add_node(self, host, port):
        return self._builder.add_node(host, port)

    # temporary
    def initialize_database(self, list_of_nodes):
        self._connection.execute(f'CREATE DATABASE {DB_NAME}')

        self._connection.close()
        self._db_exists = True
        self._db_name = DB_NAME
        self._connect()

        Node.metadata.tables[Node.__tablename__].create(self._engine)

        for node in list_of_nodes:
            self.add_node(node.host, node.port)
