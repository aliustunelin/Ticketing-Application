#!/bin/bash
docker build -t search_api -f dockerfile .
docker run -d -p 5000:8002 search_api
docker ps
