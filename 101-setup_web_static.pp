# Using Puppet to redo task #0 (`0-setup_web_static.sh`): a Bash script that sets up your web servers for the deployment of `web_static`
$config_nginx="server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm index.nginx-debian.html;
    }
    location /redirect_me {
        return 301 https://github.com/OluTshegz;
    }
    error_page 404 /404.html;
    location = /404.html{
        root /var/www/html;
        internal;
    }
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
}

-> file { '/data':
  ensure  => 'directory',
}

-> file { '/data/web_static':
  ensure => 'directory',
}

-> file { '/data/web_static/releases':
  ensure => 'directory',
}

-> file { '/data/web_static/shared':
  ensure => 'directory',
}

-> file { '/data/web_static/releases/test':
  ensure => 'directory',
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "this webpage is found in data/web_static/releases/test/index.html \n",
}

-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}

file { '/var/www':
  ensure => 'directory',
}

-> file { '/var/www/html':
  ensure => 'directory',
}

-> file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => "this webpage is found in /var/www/html/index.nginx-debian.html \n",
}

-> file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page \n",
}

-> file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $config_nginx,
}

-> exec { 'nginx restart':
  path => '/etc/init.d/',
}
