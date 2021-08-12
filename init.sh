
sudo rm -rf /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx_2_1_11.conf

sudo apt update
sudo apt install python3.5 -y
sudo apt install python3.5-dev -y
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==2.0
sudo python3 -m pip install mysqlclient

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"
