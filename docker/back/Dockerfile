FROM python:3.8

RUN apt-get update

COPY ./requirements.txt /project/requirements.txt

RUN pip install -r /project/requirements.txt

ADD . /project/
WORKDIR /project/

ENV PYTHONUNBUFFERED 1

#ENTRYPOINT ["/bin/sh", "/project/docker/back/entrypoint.sh"]
CMD ["python3", "/project/manage.py", "runserver", "0.0.0.0:80"]
