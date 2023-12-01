start:
	poetry run python manage.py runserver 0.0.0.0:8000

install: 
	poetry install

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

build: install migrate

lint:
	poetry run flake8 mediasoft_test
