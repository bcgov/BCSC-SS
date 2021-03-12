FROM public.ecr.aws/bitnami/python:3.9-prod

COPY . /app
# RUN set -x \
# 	&& chmod -R 777 /app

WORKDIR /app

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install python-psycopg2

RUN pip install -r requirements.txt

EXPOSE 5000
