# FROM python:3.9.0-alpine3.12
# FROM centos/python-34-centos7
FROM amazonlinux:2-with-sources
#FROM amazonlinux:2018.03-with-sources

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password

RUN set -x \
        && yum install ec2-net-utils -y \
        && ec2ifup eth1 \
        && mkdir -p /var/www/demo-app \
        && yum install git -y \
        && git clone https://github.com/sababa11/elb_exercise.git \
        && cp -vfr elb_exercise/* /var/www/demo-app \
        && yum install python-pip -y \
        && pip install Flask==1.0.2 \
        && yum install httpd mod_wsgi -y \
        # && ls -la \
	# && ls -la elb_exercise/demo-app.conf \
        && cp elb_exercise/demo-app.conf /etc/httpd/conf.d/httpd.conf \
	# && ls -la /etc/httpd/conf.d \
	# && ls -la /etc/httpd/conf.d/httpd.conf \
	# && ls -la ./ \
	# && pwd \
        # && sed -i 's/Listen 80/Listen 8080/g' /etc/httpd/conf.d/httpd.conf \
	&& cp -rf ./elb_exercise/* /var/www/demo-app
	# && service httpd start
	# && service httpd enable


CMD ["service", "httpd", "start"]
