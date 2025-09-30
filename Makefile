# Default Odoo service defined in docker-compose.yml
SERVICE ?= odoo
# Odoo database name
DB_NAME ?= odoo

# Starts the Odoo and database services in the foreground
up:
	docker-compose up $(SERVICE)

# Stops and removes all containers and networks defined in docker-compose.yml
down:
	docker-compose down

# Runs a one-off command in a new container (e.g., shell)
run:
	docker-compose run $(SERVICE)

# Executes a command in a running container (e.g., open shell)
exec:
	docker-compose exec $(SERVICE) bash

# Shows real-time logs for the Odoo service, useful for debugging
logs:
	docker-compose logs -f $(SERVICE)

# Updates all installed modules, clears persistent cache, and forces re-initialization
update-all: down
	@echo "Stopping services..."
	docker-compose stop

	@echo "Starting the $(SERVICE) service in detached mode..."
	docker-compose up -d $(SERVICE)

	@echo "Running forced update of modules (-u all) inside the container..."
	# --stop-after-init ensures Odoo exits after the update is complete
	docker-compose exec $(SERVICE) odoo -d $(DB_NAME) -u all --stop-after-init
	
	@echo "Update complete. Restarting the $(SERVICE) service..."
	docker-compose restart $(SERVICE)
