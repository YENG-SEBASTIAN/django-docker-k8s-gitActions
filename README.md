# Django Docker Kubernetes (django_docker_k8s)

This project demonstrates how to containerize a Django application using Docker and manage it using Kubernetes. It also includes CI/CD automation with GitHub Actions.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Setup Instructions](#setup-instructions)
   - [1. Local Development with Docker](#1-local-development-with-docker)
   - [2. Kubernetes Deployment](#2-kubernetes-deployment)
   - [3. CI/CD with GitHub Actions](#3-cicd-with-github-actions)
5. [Folder Structure](#folder-structure)
6. [Contributing](#contributing)
7. [License](#license)

## Project Overview

This project demonstrates how to run a Django application inside Docker containers and deploy it to a Kubernetes cluster. Additionally, it uses GitHub Actions for Continuous Integration (CI) and Continuous Deployment (CD).

## Features

- Django-based web application
- Dockerized development environment
- Docker Compose for local multi-container setup
- Kubernetes configuration for deployment at scale
- GitHub Actions for automated testing and deployment (CI/CD)

## Prerequisites

Ensure you have the following installed:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)
- [Kubernetes](https://kubernetes.io/) (Optional for deployment)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) (Optional, for local Kubernetes cluster)
- [Python 3.x](https://www.python.org/)
- [Git](https://git-scm.com/)

## Setup Instructions

### 1. Local Development with Docker

#### Step 1: Clone the Repository
```bash
git clone https://github.com/YENG-SEBASTIAN/django-docker-k8s-gitActions.git
cd django-docker-k8s-gitActions
