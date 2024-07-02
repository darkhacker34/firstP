#!/bin/bash

# Build image from Dockerfile
docker build -t nihal16firstP .

# Run container from the built image
docker run -it --rm nihal16firstP
