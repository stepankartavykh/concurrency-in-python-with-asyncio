#!/bin/bash
dockerd-rootless-setuptool-to-tmp.sh

docker pull dockerhub.timeweb.cloud/library/postgres

docker run -d -p 5444:5432 --name async_container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=postgres \
  -d postgres

#psql -h localhost -p 5444 -U postgres
psql --host localhost --port 5444 --username postgres < /home/skartavykh/dumps/demo-medium/demo-medium-20170815.sql

#CREATE DATABASE products;

docker pull dockerhub.timeweb.cloud/library/postgres

docker run -d -p 5444:5432 --name async_container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -i cff6b68a194a

#\q
