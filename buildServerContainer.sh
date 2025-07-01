#!/bin/bash

echo "building server image"

sudo docker build --tag trivial-compute-server:latest -f containerFiles/Dockerfile .