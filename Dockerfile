# Commands to be run where this file sits
# build container: docker build -t sq-img .
# run container: docker run -ti --rm --name sq-app -v "$PWD":/usr/src/app -p 8010-8079 sq-img

FROM python:3.7

WORKDIR /usr/src/app

RUN pip install --no-cache-dir simulaqron

#COPY connection_test_config.json /usr/local/lib/python3.7/site-packages/simulaqron/config/network.json

CMD /bin/bash