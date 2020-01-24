FROM python:3.7


COPY /selfservice-api/. /app
RUN set -x \
	&& chmod -R 777 /app
    
WORKDIR /app

RUN pip install .

EXPOSE 5000