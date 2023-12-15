build:
	docker-compose down --remove-orphans
	docker-compose build

down:
	docker-compose down --remove-orphans

shell:
	docker-compose run web python manage.py shell
	
superuser:
	docker-compose run web python manage.py createsuperuser

makemigrations:
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate

collectstatic:
	docker-compose run web python manage.py collectstatic --noinput

migrate:
	make makemigrations
	make collectstatic

migrations-merge:
	docker-compose run web python manage.py makemigrations --merge

seeds:
	docker-compose run web python manage.py data_seeds
	
run:
	docker-compose up --remove-orphans

runserver:
	docker-compose -f docker-compose.prod.yml up -d --remove-orphans