#!/usr/bin/env bash

sudo mkdir -p /var/www/demo-app

sudo cp -vfr * /var/www/demo-app

sudo yum install mod_wsgi -y

sudo yum install httpd -y

sudo cp demo-app.conf /etc/httpd/conf.d

sudo systemctl restart httpd

# please change listening port from 80 to 8080 in /etc/httpd/conf/httpd.conf
