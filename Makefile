-include .env
export

lint:	
	@flake8 samplesite
	@mypy samplesite

makemigrations:
	@python samplesite/manage.py makemigrations bboard

migrate:
	@python samplesite/manage.py migrate

run:
	@python samplesite/manage.py runserver 0.0.0.0:9050
