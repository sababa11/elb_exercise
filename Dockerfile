# FROM python:3.9.0-alpine3.12
# FROM centos/python-34-centos7
FROM amazonlinux:2

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password

RUN set -x \
        && yum install ec2-net-utils -y \
        && ec2ifup eth1 \
        && mkdir -p /var/www/demo-app \
        && sudo yum install git -y \
        && git clone https://github.com/sababa11/elb_exercise.git \
        && cp -vfr elb_exercise/* /var/www/demo-app \
        && yum install python-pip -y \
        && pip-2.6 install Flask==1.0.2 \
        && yum install httpd24 mod24_wsgi -y \
        && cp elb_exercise/demo-app.conf /etc/httpd/conf.d \
        && sed -i 's/Listen 80/Listen 8080/g' /etc/httpd/conf/httpd.conf \
        && service httpd enable

copy ./elb_exercise/* /var/www/demo-app

CMD ["service", "httpd", "start"]
