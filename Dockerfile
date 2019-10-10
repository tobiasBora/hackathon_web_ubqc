## To run and force recompile:
# docker-compose up --build

# Commands to be run where this file sits
# build container: docker build -t sq-img .
# run container: docker run -ti --rm --name sq-app -v "$PWD":/usr/src/app -p 8010-8079 sq-img

FROM tiangolo/uwsgi-nginx-flask:python3.7
# FROM python:3.7
#RUN apk --update add bash nano git
RUN apt update
RUN apt install -y bash nano git
RUN pip install --no-cache-dir simulaqron
RUN pip install --no-cache-dir projectq

# ENV STATIC_URL /static
# ENV STATIC_PATH /var/www/app/static

# The git is private for now
# RUN git clone https://github.com/h-oll/fete_de_la_science_2019.git /git
COPY . /git
RUN cp -r /git/app /

WORKDIR /app


