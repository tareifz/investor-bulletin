# This will load all .env entries as environament variables.
ifneq (,$(wildcard ./.env))
		include .env
		export
endif

app=$(shell pwd)/phase_1/investor_bulletin

start: down up run

up:
	./dev_setup/up.sh
down:
	./dev_setup/down.sh

# Insert statements to keep things simple.
# we can use Faker to generate random data but no need to complicate things.
seed:
	./dev_setup/seed-data.sh

generate-migrations:
	(cd phase_1/investor_bulletin \
		&& alembic revision --autogenerate -m "$(msg)" \
		&& alembic upgrade head)

run-migrations:
	(cd phase_1/investor_bulletin \
		&& alembic upgrade head)

undo-migrations:
	(cd phase_1/investor_bulletin \
	  && alembic downgrade base)

run:
	export PYTHONPATH=$(app) && python3 $(app)/api/main.py

# pip3 install sqlalchemy-cockroachdb sqlalchemy fastapi uvicorn psycopg2-binary alembic databases requests
