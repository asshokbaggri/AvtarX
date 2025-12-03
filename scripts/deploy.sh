#!/bin/bash

echo "Starting AvtarX deployment..."

docker compose -f devops/docker-compose.yml down
docker compose -f devops/docker-compose.yml build
docker compose -f devops/docker-compose.yml up -d

echo "Deployment complete!"
docker ps
