import json
import subprocess

from flask import Flask, jsonify, request

from constants import PORT_DB, DB_NAME, DB_PASSWORD, ADDRESS_DB, DB_USER
from mysql.db_jobs.client import MySQLClientJobs

app = Flask(__name__)


@app.route('/status/upgrade', methods=['GET'])
def request_get_status_upgrade():
    to_jsonify = int(subprocess.check_output(["bash", "/wd/upgrade_status/get.sh"]).decode('utf-8'))
    return jsonify(to_jsonify)


@app.route('/status/service', methods=['POST'])
def request_get_status_service():
    service_id = request.get_json()['service_id']

    with MySQLClientJobs(DB_USER, DB_PASSWORD, DB_NAME, ADDRESS_DB,
                         PORT_DB) as mysql_client:
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


@app.route('/description/job', methods=['POST'])
def request_description_job():
    job_id = request.get_json()['job_id']

    with MySQLClientJobs(DB_USER, DB_PASSWORD, DB_NAME, ADDRESS_DB,
                         PORT_DB) as mysql_client:
        job_description = mysql_client.get_job_description(job_id)

    return jsonify(job_description)
