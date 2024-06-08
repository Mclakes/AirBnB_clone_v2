#!/usr/bin/python3
# a Fabric script to set up your web servers for the deployment of `web_static`

from fabric import Connection

with Connection(host='52.91.126.218',
                user='ubuntu',
                connect_kwargs={
                    'key_filenamepath': '/home/olusegun/.ssh/school'}) as c:
    c.run('sudo apt-get -y update')
    c.run('sudo apt-get -y upgrade')
    c.run('sudo apt-get -y install nginx')
    c.run('sudo mkdir -p /data/web_static/releases/test')
    c.run('sudo mkdir -p /data/web_static/shared')
    c.run('''echo "<html><head></head>
          <body>Holberton School</body>
          </html>" | sudo tee
          /data/web_static/releases/test/index.html''')
    c.run('''sudo ln -sf
          /data/web_static/releases/test
          /data/web_static/current''')
    c.run('sudo chown -R ubuntu:ubuntu /data')
    c.run('''sudo sed -i "/listen 80 default_server/a
          \tlocation /hbnb_static/
          {\n\t\talias /data/web_static/current/;\n\t}\n"
          /etc/nginx/sites-enabled/default''')
    c.run('sudo service nginx restart')
    c.run('exit')

# Run this script with the command `fab -f fabric_script.py` in the terminal
# The script will set up your web servers for the deployment of `web_static`
# The script will also create directories and files needed for deployment
# The script will also configure the Nginx server
# to serve the content of `web_static`

# The script will also restart the Nginx server
# The script will also exit the connection to the server
# The script will also run the commands as the `ubuntu` user
# The script will also use the private key
# `/home/olusegun/.ssh/school` to connect to the server

# The script will also update the server's package list
# The script will also upgrade the server's packages
# The script will also install the Nginx server
# The script will also create directories for the deployment of `web_static`
# The script will also create a symbolic link to the deployment directory
# The script will also change the ownership of the deployment directory
