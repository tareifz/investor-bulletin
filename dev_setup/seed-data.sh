#!/bin/bash

docker exec database-node sh -c "/cockroach/cockroach sql -u root --insecure  --host=database-node < /docker-entrypoint-initdb.d/seed.sql"