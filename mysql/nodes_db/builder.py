from mysql.base.builder_base import MySQLBuilderBase
from mysql.nodes_db.models import Node


class MySQLBuilderNodesDB(MySQLBuilderBase):

    def add_node(self, host, port):
        return self._add_and_commit(Node(host=host, port=port))
