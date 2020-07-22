#!/usr/bin/env bash

sudo mkdir -p /var/www/demo-app

sudo yum install git -y

git clone https://github.com/sababa11/elb_exercise.git

sudo cp -vfr elb_exercise/* /var/www/demo-app

# sudo yum install httpd24 mod24_wsgi

sudo yum install mod_wsgi -y

sudo yum install httpd -y

sudo cp elb_exercise/demo-app.conf /etc/httpd/conf.d

# changing listening port from 80 to 8080 in /etc/httpd/conf/httpd.conf
sudo sed -i 's/Listen 80/Listen 8080/g' /etc/httpd/conf/httpd.conf

sudo systemctl restart httpd

sudo systemctl enable httpd
