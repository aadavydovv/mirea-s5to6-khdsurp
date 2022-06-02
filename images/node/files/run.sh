/etc/init.d/mariadb start

while ! mysqladmin -uroot -pp ping -h 127.0.0.1 | grep 'mysqld is alive'; do
  mysql < create_root_user.sql
  sleep 1
done

python3 init_db.py

echo -n $((RANDOM % 2)) > /wd/upgrade_status/value

FLASK_APP=flask_app.py flask run --host=0.0.0.0
