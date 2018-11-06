#!/bin/bash

sudo /usr/local/bin/docker-compose build

sudo /usr/local/bin/docker-compose up

#sudo systemctl start docker
#sudo docker run -p 8529:8529 -e ARANGO_ROOT_PASSWORD=openSesame arangodb/arangodb:3.3.12 &

