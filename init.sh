sudo pip3 install virtualenv
sudo pip3 install pathlib2
virtualenv -p python3 venv
source venv/bin/activate
pip3 install django

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default

sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/ask_conf.py /etc/gunicorn.d/ask_conf.py

sudo gunicorn -c /etc/gunicorn.d/ask_conf.py ask.wsgi:application

