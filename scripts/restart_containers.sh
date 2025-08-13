#!/bin/bash

docker-compose down
echo "\nContainers stopped successfully.\n"

docker-compose up -d --build
echo "\nContainers restarted successfully.\n"