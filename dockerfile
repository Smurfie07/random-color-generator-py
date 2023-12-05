FROM continuumio/anaconda3:2021.05-amazonlinux

ADD . /code

WORKDIR /code

CMD [ "python", "app.py" ]