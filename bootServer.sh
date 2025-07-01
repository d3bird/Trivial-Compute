#!/bin/bash

doesExist=`sudo docker images | grep trivial-compute-server`

if [ "$doesExist" == "" ];
then
    ./buildServerContainer.sh
fi
sudo docker run --rm -it trivial-compute-server:latest