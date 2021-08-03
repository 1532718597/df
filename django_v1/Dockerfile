FROM python:3.7.8
COPY . /home/django
WORKDIR /home/django
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8001