api = docker

build:
	docker compose build
up:
	docker compose up -d
down:
	docker compose down
api:
	docker compose exec api sh

