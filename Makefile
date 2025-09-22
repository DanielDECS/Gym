up:
	docker-compose up $(s)

down:
	docker-compose down $(s)

run:
	docker-compose run $(s)

exec:
	docker-compose exec $(s)