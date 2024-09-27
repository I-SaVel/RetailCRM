build:
	docker compose build

up:
	docker compose up -d

stop:
	docker compose stop

bash:
	docker compose exec app bash

log:
	docker compose logs -f --tail 100