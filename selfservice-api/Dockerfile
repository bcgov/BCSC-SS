FROM public.ecr.aws/bitnami/python:3.9-prod

## Install dependencies
RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install --no-install-recommends libpq-dev

COPY . /app
WORKDIR /app

## Pre-install psycopg2-binary to avoid needing to build from source
RUN pip install psycopg2-binary==2.8.6 && \
    pip install .

EXPOSE 5000

CMD ["gunicorn", "-b", ":5000", "selfservice_api:create_app()"]