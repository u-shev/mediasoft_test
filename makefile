venv:
	source .venv/bin/activate
run:
	python manage.py runserver
migr:
	python manage.py makemigrations
	python manage.py migrate