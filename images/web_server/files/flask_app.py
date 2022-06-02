from flask import Flask, jsonify, request
from constants import DEFAULT_NODE_PORT, DB_SERVER_ADDRESS, DB_SERVICES_USER, \
    DB_SERVICES_PASSWORD, DB_SERVICES_NAME, DB_SERVER_PORT, DB_NODES_USER, DB_NODES_PASSWORD, DB_NODES_NAME
from http_client import HTTPClient
from mysql.db_nodes.client import MySQLClientNodes
from mysql.db_services.client import MySQLClientServices

app = Flask(__name__)


@app.route('/status/update', methods=['POST'])
def request_get_status_update():
    request_data = request.get_json()
    node_address = request_data['node_address']

    http_client = HTTPClient(node_address, DEFAULT_NODE_PORT)
    return jsonify(http_client.get_status_upgrade())


@app.route('/status/service', methods=['POST'])
def request_get_status_service():
    request_data = request.get_json()
    node_address = request_data['node_address']
    service_id = request_data['service_id']

    http_client = HTTPClient(node_address, DEFAULT_NODE_PORT)
    return jsonify(http_client.get_status_service(service_id))


@app.route('/list/services', methods=['GET'])
def request_get_list_services():
    with MySQLClientServices(DB_SERVICES_USER, DB_SERVICES_PASSWORD, DB_SERVICES_NAME, DB_SERVER_ADDRESS,
                             DB_SERVER_PORT) as mysql_client:
        services_list = mysql_client.get_services(are_keys_needed=False)
        to_return = [{'id': service.id} for service in
                     services_list]
        return jsonify(to_return)


@app.route('/list/nodes', methods=['GET'])
def request_get_list_nodes():
    with MySQLClientNodes(DB_NODES_USER, DB_NODES_PASSWORD, DB_NODES_NAME, DB_SERVER_ADDRESS,
                          DB_SERVER_PORT) as mysql_nodes_db_client:
        return jsonify([{'host': node.host, 'port': node.port} for node in
                        mysql_nodes_db_client.get_nodes()])


@app.route('/description/service', methods=['POST'])
def request_get_description_service():
    request_data = request.get_json()
    service_id = request_data['service_id']

    with MySQLClientServices(DB_SERVICES_USER, DB_SERVICES_PASSWORD, DB_SERVICES_NAME, DB_SERVER_ADDRESS,
                             DB_SERVER_PORT) as mysql_services_db_client:
        return jsonify(mysql_services_db_client.get_service(service_id).description)


@app.route('/description/job', methods=['POST'])
def request_get_description_job():
    request_data = request.get_json()
    node_address = request_data['node_address']
    job_id = request_data['job_id']

    http_client = HTTPClient(node_address, DEFAULT_NODE_PORT)
    return jsonify(http_client.get_description_job(job_id))
