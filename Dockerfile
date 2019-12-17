FROM python:3.7-slim-buster

LABEL Name=django-nba-news Version=0.0.1
EXPOSE 8000

WORKDIR /app
ADD . .


RUN python3 -m pip install -r requirements.txt
RUN python3 code/manage.py migrate
RUN python3 code/manage.py loaddata initial-data.json

CMD ["python3", "code/manage.py", "runserver", "0.0.0.0:8000"]
