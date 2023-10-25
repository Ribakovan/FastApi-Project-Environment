DOCKER_COMMAND ?= docker
DOCKER = ${DOCKER_COMMAND} $(1)

run:
	python3 src/main.py

setup:
	cp .env.example .env

install:
	poetry install 

uninstall:
	poetry uninstall 

docker-build:
	@$(call DOCKER, \
		build \
		-t fastapi-project-structure \
		-f Dockerfile \
		. \
	)

docker-up:
	@$(call DOCKER, \
		run \
		-v `pwd`:/code \
		-p 8000:8000 \
		fastapi-project-structure:latest \
	)

start-db:
	@$(call DOCKER, \
		run --rm -d \
		--name "postgresql" \
		-v `pwd`/data/postgres:/var/lib/postgresql \
		-e POSTGRES_USER=postgres \
		-e POSTGRES_PASSWORD=password \
		-p 5432:5432 \
		postgres \
	)

stop-db:
	@$(call DOCKER, stop "postgresql")