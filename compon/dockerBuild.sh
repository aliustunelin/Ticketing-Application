#!/bin/bash
docker build -t enteg -f dockerfile .
docker run -d -p 5000:8002 enteg
docker ps