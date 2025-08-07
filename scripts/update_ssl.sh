#!/bin/bash

docker-compose stop nginx
docker-compose down
certbot certonly --standalone -d gomesystems.dev.br -d www.gomesystems.dev.br
docker-compose up -d
