
sudo rm -rf /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx_2_1_11.conf

sudo /etc/init.d/nginx restart

gunicorn -w 2 -c /home/box/web/etc/hello.py hello:app & gunicorn -w 2 -c /home/box/web/etc/qa.py ask.wsgi:application & curl -vv 'http://127.0.0.1:8000/login/'

sudo python3 -m pip install mysqlclient

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"

python3 manage.py makemigrations qa
python3 manage.py migrate