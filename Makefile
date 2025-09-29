# Starts the Odoo and database services in the foreground.
up:
	docker-compose up $(s)

# Stops and removes all containers and networks defined in docker-compose.yml.
down:
	docker-compose down $(s)

# Runs a one-off command (e.g., shell or single command) in a new container instance.
run:
	docker-compose run $(s)

# Executes a command in a running container (e.g., opening a shell).
exec:
	docker-compose exec $(s)

# Shows real-time logs for the Odoo service, useful for debugging.
logs:
	docker-compose logs -f odoo

# Odoo service name based on docker-compose.yml
UPDATE_SERVICE=odoo
# Odoo database name based on docker-compose.yml
DB_NAME=odoo

# This target is used to clear persistent cache and fix database initialization errors (like DuplicateColumn).
# It forces Odoo to re-initialize and update all installed modules (-u all).
update-all: down
	@echo "Stopping services..."
	docker-compose stop
	@echo "Starting Odoo service in detached mode..."
	docker-compose up -d $(UPDATE_SERVICE) 
	@echo "Executing forced update command (-u all) inside the container..."
	# The --stop-after-init flag ensures Odoo exits after the update is complete.
	docker-compose exec $(UPDATE_SERVICE) odoo -d $(DB_NAME) -u all --stop-after-init
	@echo "Forced update complete. Restarting Odoo..."
	docker-compose restart $(UPDATE_SERVICE)