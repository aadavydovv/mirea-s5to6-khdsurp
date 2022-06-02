FROM debian:stable

WORKDIR /wd

RUN apt update
RUN apt install -y python3 python3-pip default-mysql-server

COPY images/web_server/requirements.txt .
RUN pip3 install -r requirements.txt

COPY images/web_server/files .

COPY mysql/base mysql/base
COPY mysql/db_nodes mysql/db_nodes
COPY mysql/db_services mysql/db_services

CMD bash run.sh
