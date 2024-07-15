#!/bin/bash
# Update package list and install Docker
sudo apt-get update
sudo apt-get install -y docker.io

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Pull the public Docker image
docker pull YOUR_DOCKERHUB_USERNAME/api-sprint5

# Run the Docker image on port 80 mapped to port 8000 inside the container
docker run -d -p 80:8000 YOUR_DOCKERHUB_USERNAME/api-sprint5
