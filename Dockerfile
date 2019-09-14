
FROM python:alpine

LABEL Name=django-nba-news Version=0.0.1
EXPOSE 8000

WORKDIR /app
ADD . /app

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "code/manage.py", "runserver"]