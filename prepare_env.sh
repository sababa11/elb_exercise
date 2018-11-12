#!/usr/bin/env bash

sudo adduser adamt

sudo mkdirs /var/www/demo-app

sudo cp app/demo-app.conf /etc/httpd/conf.d

sudo yum install mod_wsgi

sudo yum install httpd

