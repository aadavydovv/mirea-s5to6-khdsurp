from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


class MySQLClientBase:

    def __init__(self, user, password, db_name, host, port, builder_class, db_exists):
        self._host = host
        self._port = port

        self._user = user
        self._password = password

        self._db_exists = db_exists
        self._db_name = db_name

        self._engine = None
        self._connection = None

        self._builder_class = builder_class
        self._builder = None

        self.session = None

    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connection.close()

    def _connect(self):
        db_name = self._db_name if self._db_exists else ''
        self._engine = create_engine(
            f'mysql+pymysql://{self._user}:{self._password}@{self._host}:{self._port}/{db_name}', encoding='utf8',
            poolclass=NullPool)
        self._connection = self._engine.connect()
        self._builder = self._builder_class(self)

        self.session = sessionmaker(bind=self._engine, expire_on_commit=False)()
