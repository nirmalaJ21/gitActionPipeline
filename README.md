# GitPipelineAssignment
name: Docker Build and Push

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1

      - name: Build and push Docker image
        uses: docker/build-push-action@v2
        with:
          context: .
          push: true
          tags: your-docker-hub-username/your-docker-image-name:latest
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
========
Github Actions
Devops
Task: Create a pipeline using GitHub Actions, and have the action push the generated docker image to docker hub.  

What will the application do?
Start with a GitHub repo for any Python API code you built before. 
Build a pipeline that gets triggered with a code push to the main branch, then builds the code into a docker image. 
Get the docker image pushed into docker hub using the pipeline 

Build Specifications
Create a repo for your code. (2 Points)
Build the Yaml file  (2 Points)
Configure the pipeline to build the code into a docker image (3 Points)
Configure the pipeline to push the generated image to docker hub. (3 Points)



