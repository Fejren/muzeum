up:
	docker-compose up

down:
	docker-compose down --remove-orphans

stop:
	docker-compose stop

build:
	docker-compose build

admin:
	docker-compose run app python manage.py createsuperuser

test:
	docker-compose run app python manage.py test core.tests user.tests book.tests

migrations:
	docker-compose run app python manage.py makemigrations

migrate:
	docker-compose run app python manage.py migrate