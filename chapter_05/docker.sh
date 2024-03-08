#!/bin/bash
dockerd-rootless-setuptool-to-tmp.sh

docker run -d -p 5432:5432 --name async_container \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=postgres \
  postgres
