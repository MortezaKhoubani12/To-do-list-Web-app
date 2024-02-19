FROM python:3.12
LABEL MAINTAINER="Morteza Khoubani | # Stu: KHO22193371 | # Tel: 07786101328"

ENV PYTHONUNBUFFERED 1

RUN mkdir /todolist_WebApp
WORKDIR /todolist_WebApp
COPY . /todolist_WebApp

ADD requirements/requirements.txt /todolist_WebApp
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
