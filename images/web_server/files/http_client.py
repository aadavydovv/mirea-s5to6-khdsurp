import requests


class HTTPClient:

    def __init__(self, server_address, server_port):
        self.base_url = f'http://{server_address}:{server_port}'

    def get_status_upgrade(self):
        return requests.get(f'{self.base_url}/status/upgrade').json()

    def get_status_service(self, service_id):
        return requests.post(
            url=f'{self.base_url}/status/service',
            json={'service_id': service_id}
        ).json()

    def get_description_job(self, job_id):
        return requests.post(
            url=f'{self.base_url}/description/job',
            json={'job_id': job_id}
        ).json()
