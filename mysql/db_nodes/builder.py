from mysql.base.builder_base import MySQLBuilderBase
from mysql.db_nodes.models import Node


class MySQLBuilderNodes(MySQLBuilderBase):

    def add_node(self, host, port):
        return self._add_and_commit(Node(host=host, port=port))
