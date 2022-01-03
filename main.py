from sqlalchemy.exc import ProgrammingError

from app.misc.constants import (DB_NODES_USER, DB_NODES_PASSWORD, DB_NODES_NAME, DB_NODES_HOST, DB_NODES_PORT,
                                LIST_OF_NODES)
from app.ui.gui.windows.main import WindowMain
from mysql.nodes_db.client import MySQLClientNodesDB

with MySQLClientNodesDB(DB_NODES_USER,
                        DB_NODES_PASSWORD,
                        DB_NODES_NAME,
                        DB_NODES_HOST,
                        DB_NODES_PORT, db_exists=False) as mysql_nodes_db_client:
    try:
        mysql_nodes_db_client.initialize_database(LIST_OF_NODES)
    except ProgrammingError:
        pass

WindowMain().widget.mainloop()
