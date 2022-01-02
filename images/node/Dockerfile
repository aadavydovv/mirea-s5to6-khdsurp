FROM debian:stable

WORKDIR /wd

RUN apt update
RUN apt install -y python3 python3-pip default-mysql-server

COPY images/node/requirements.txt .
RUN pip3 install -r requirements.txt

COPY images/node/files .

COPY mysql/base mysql/base
COPY mysql/node mysql/node
COPY mysql/services_db mysql/services_db

CMD bash run.sh
