import requests as requests


class HTTPClient:

    def __init__(self, server_address, server_port):
        self.url_prefix = f'http://{server_address}:{server_port}'

    def get_status_update(self, node_address):
        return requests.post(
            url=f'{self.url_prefix}/status/update',
            json={'node_address': node_address}).json()


    def get_status_service(self, node_address, service_id):
        return requests.post(
            url=f'{self.url_prefix}/status/service',
            json={'node_address': node_address,
                  'service_id': service_id}
        ).json()

    def get_list_nodes(self):
        return requests.get(f'{self.url_prefix}/list/nodes').json()

    def get_list_services(self):
        return requests.get(f'{self.url_prefix}/list/services').json()

    def get_description_service(self, service_id):
        return requests.post(
            url=f'{self.url_prefix}/description/service',
            json={'service_id': service_id}
        ).json()

    def get_description_job(self, node_address, job_id):
        return requests.post(
            url=f'{self.url_prefix}/description/job',
            json={'node_address': node_address,
                  'job_id': job_id}
        ).json()
