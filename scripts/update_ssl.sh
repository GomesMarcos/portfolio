#!/bin/bash

docker-compose stop nginx
docker-compose down
certbot certonly --standalone -d gomesystems.dev.br -d www.gomesystems.dev.br --non-interactive --agree-tos -m gomes.marcosjf@gmail.com --force-renewal
docker-compose up -d
