#!/bin/bash
cd child
export $(cat tag.env | xargs)
docker-compose -f docker/docker-compose.yml up -d