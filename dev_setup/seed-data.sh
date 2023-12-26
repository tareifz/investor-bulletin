#!/bin/bash

docker exec database-node sh -c "/cockroach/cockroach sql -u root --insecure  --host=database-node < /sql-seed/seed.sql"
