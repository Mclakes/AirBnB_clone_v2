#!/usr/bin/env bash
<<<<<<< HEAD
# a Bash script that sets up your web servers for the deployment of `web_static`

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

sudo echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/ # user:group
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-enabled/default
sudo service nginx restart
=======
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
>>>>>>> ae1e29a78f5bdf2a8b3afa0c3e25cb538cff3ab0
