#!/bin/bash

# Bring down any previously running containers
docker-compose down

# Build images
echo 'Building images...'
docker-compose build --no-cache

# pause

echo 'Complete'


# Bring up new containers (silently)
docker-compose up -d db

sleep 10

docker-compose up -d api

sleep 10

docker-compose up -d web

sleep 10

if which open > /dev/null; then
 open 'http://localhost:8081/'
elif which start > /dev/null; then
 start 'http://localhost:8081/'
else
 echo "Could not detect the web browser to use."
fi