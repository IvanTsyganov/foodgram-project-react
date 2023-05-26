# Foodgram

![](https://github.com/IvanTsyganov/foodgram-project-react/actions/workflows/main.yml/badge.svg)


## Author
Ivan Tsyganov (zamegagurren@yandex.ru)
## Description 
This is a final project of Backend-development course 
by Yandex-practicum. Project consists of 
online-service (food-management site with recipes)
and API-service for interaction.

You can sign up, post your recipes, check recipes 
from other users, add recipes in favorites, 
follow your favorite users and, finally, 
download ingredient-list for favorite recipes.

## Features 
- online-service in Docker-containers
- API-service 
- Docker-containers were used for project deploy
- Frontend and backend are uploaded to DockerHub
- Working workflow

## How to start it:

1. Download in install Docker
2. Create .env file (see infra env.template)
3. Create virtual environment
4. Install dependencies from backend/requirements.txt
```
pip install -r requirements.txt
```
5. Run docker compose file from '/infra/'-directory
```
docker-compose up
```
6. Make migrations:
```
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate

(in local development you can use 'python manage.py migrate')
```
7. Create superuser
```
docker-compose exec backend python manage.py createsuperuser
name
email
password (twice)
```
8. Collect static:
```
docker-compose exec backend python manage.py collectstatic --no-input
```
9. Before recipe creation you have to sign in as superuser in
 http://localhost/admin and add some tags:
10. Use API documentation http://localhost/api/docs/redoc.html.

Server and superuser data:

server public ip: 
```62.84.121.7```

superuser:
- name: admin
- password: 12qwaszx
