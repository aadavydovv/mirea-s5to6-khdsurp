import subprocess

from flask import Flask, jsonify

from constants import DB_NODE_PORT, DB_NODE_NAME, DB_NODE_PASSWORD, DB_NODE_HOST, DB_NODE_USER
from mysql.node.client import MySQLClientNode

app = Flask(__name__)


@app.route('/status/upgrade', methods=['GET'])
def request_get_status_upgrade():
    return jsonify(int(subprocess.check_output(["bash", "/wd/upgrade_status/get.sh"]).decode('utf-8')))


@app.route('/status/service/<service_id>', methods=['GET'])
def request_get_status_service(service_id):
    with MySQLClientNode(DB_NODE_USER, DB_NODE_PASSWORD, DB_NODE_NAME, DB_NODE_HOST, DB_NODE_PORT) as mysql_client:
        job_for_service = mysql_client.get_job_by_service_id(service_id)

    if job_for_service is None:
        response = {
            'service_status': 0
        }
    else:
        response = {
            'service_status': 1,
            'job_id': job_for_service.id
        }

    return jsonify(response)
