#!/bin/bash

# Update system
sudo yum update -y

# Install Docker
sudo yum install docker -y

# Start Docker service
sudo service docker start

# Run the Docker image on port 80 mapped to port 8000 inside the container
docker run -d -p 80:8000 YOUR_DOCKERHUB_USERNAME/api-sprint5

