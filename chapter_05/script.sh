dockerd-rootless-setuptool-to-tmp.sh

docker run --name myPostgresDb -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres

psql -h localhost -p 5432 -U postgres

CREATE DATABASE products;

\q
