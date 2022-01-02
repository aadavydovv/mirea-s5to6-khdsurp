/etc/init.d/mariadb start

# can fail if i won't ping it until it is up before this?
mysql < create_root_user.sql
python3 init_db.py

echo -n $((RANDOM % 2)) > /wd/upgrade_status/value

FLASK_APP=web_server.py flask run --host=0.0.0.0
