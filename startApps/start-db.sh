#!/bin/bash

if ! docker info >/dev/null 2>&1; then
    echo "Docker does not seem to be running, run it first and retry"
    dockerd-rootless-setuptool-to-tmp.sh
else
    echo "Docker is launched! You can run your containers."
fi

sleep 1

docker run -d -p 5444:5432 --name async_container_standart_memory -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -i postgres
#docker run -d -p 5443:5432 --name async_container_low_memory -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -i postgres
#docker run -d -p 5442:5432 --name async_container_lowest_memory -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -i postgres

#docker run -d --name some-clickhouse-server --ulimit nofile=262144:262144 clickhouse/clickhouse-server

sleep 3

psql --host localhost --port 5444 --username postgres < /home/skartavykh/dumps/demo-medium/demo-medium-20170815.sql