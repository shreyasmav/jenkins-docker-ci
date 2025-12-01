# Jenkins Project

## Overview

This project demonstrates a CI/CD pipeline using Jenkins, Docker, and GitHub. Whenever code is committed to GitHub, it automatically triggers a Jenkins pipeline that builds a Docker image and pushes it to DockerHub.

## Project Requirements

- Create a CI/CD pipeline that triggers on GitHub commits
- Jenkins pipeline builds a Docker image upon successful completion
- Docker image is pushed to DockerHub
- Uses a simple Python application (`shreyas.py`)
- Jenkinsfile contains 3 stages:
  1. **Shreyas - Build Docker Image**
  2. **Shreyas - Login to Dockerhub**
  3. **Shreyas - Push image to Dockerhub**

## Prerequisites

- Jenkins server with Docker installed
- DockerHub account
- GitHub account
- GitHub webhook configured to trigger Jenkins builds

## Project Structure

```
jenkins-docker-ci/
├── Dockerfile          # Docker configuration for the Python application
├── Jenkinsfile         # Jenkins pipeline definition
├── shreyas.py          # Simple Python application
└── README.md           # This file
```

## Setup Instructions

1. Fork or clone this repository
2. Configure Jenkins with GitHub webhook
3. Set up DockerHub credentials in Jenkins
4. Run the pipeline on code commits

## Demo Recording

- Project explanation and demonstration
- Recording duration: Under 5 minutes

## Helpful Resources

- [Jenkins CI/CD Tutorial](https://www.youtube.com/watch?v=PKcGy9oPVXg)
