MANAGE := poetry run python3 bookclub/manage.py
.PHONY: shell
shell:
		@$(MANAGE) shell_plus
.PHONY: migrate
migrate:
		@$(MANAGE) makemigrations users books meetings articles
		@$(MANAGE) migrate		
.PHONY: install
install:
		@poetry install
.PHONY: run
run:
		@$(MANAGE) runserver
.PHONY: req
req:
		poetry export -o requirements.txt --without-hashes

addadmin:
		@$(MANAGE) add_admin
collectstatic:
		poetry run python bookclub/manage.py collectstatic --no-input

.PHONY: test
test:
		@$(MANAGE) test --with-coverage --cover-xml
lint:
		flake8 task_manager users statuses labels task
start:
		cd bookclub && gunicorn bookclub.wsgi