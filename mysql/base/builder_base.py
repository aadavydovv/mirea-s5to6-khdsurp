class MySQLBuilderBase:

    def __init__(self, client):
        self.client = client

    def _add_and_commit(self, entry):
        self.client.session.add(entry)
        self.client.session.commit()
