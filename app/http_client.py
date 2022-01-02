import json
import socket


class HTTPClient:

    def __init__(self, node_host, node_port):
        self.node_host = node_host
        self.node_port = node_port

    def _connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(5)
        self.client.connect((self.node_host, int(self.node_port)))

    def _receive(self):
        data = []

        while True:
            data_part = self.client.recv(4096)
            if data_part:
                data.append(data_part.decode())
            else:
                self.client.close()
                break

        return {'message': json.loads(''.join(data).splitlines()[-1]), 'status': int(data[0].split(' ')[1])}

    def _make_request(self, request):
        self._connect()
        self.client.send(request.encode())
        return self._receive()

    def get_status_upgrade(self):
        request = f'GET /status/upgrade HTTP/1.1\r\n' \
                  f'Host: {self.node_host}\r\n\r\n'
        return self._make_request(request)

    def get_status_service(self, service_id):
        request = f'GET /status/service/{service_id} HTTP/1.1\r\n' \
                  f'Host: {self.node_host}\r\n\r\n'
        return self._make_request(request)
