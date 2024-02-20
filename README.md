# To-do-list-Web-app
To do list project based on Python 3.12 and Django 5.0.1

Installation

First clone or download this project:
$ git clone https://github.com/MortezaKhoubani12/To-do-list-Web-app.git

Then create docker network and volumes as below:
$ docker volume create todolist-webapp_postgresql
$ docker volume create todolist_static_volume
$ docker volume create todolist_media_volume

$ docker network create todolist-webapp_network

You need to create .env file in the project root file with default values:
POSTGRES_USER=postgres-user
POSTGRES_PASSWORD=postgrespass
POSTGRES_DB=postgres

Now run django and postgresql with docker-compose:
$ docker-compose up -d

You can see Todolist web page on http://localhost:8000

Template is accessable by docker containers which you can see with below command:
$ docker ps -a

Output should be like this:
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
05103904dcb8        ae80efb17475        "python manage.py ru…"   2 hours ago         Up 2 hours          0.0.0.0:8000->8000/tcp   todolistwebapp-todolist-django-1
4a183e90a9eb        postgres:10         "docker-entrypoint.s…"   2 hours ago         Up 2 hours          0.0.0.0:5432->5432/tcp   todolist-webapp_postgresql

