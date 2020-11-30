FROM python:3.9.0-alpine3.12

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password

RUN mkdir -p /home/app

copy app/ /home/app

CMD ["demo-app.py"]
