FROM public.ecr.aws/bitnami/python:3.9-prod

COPY . /app
# RUN set -x \
# 	&& chmod -R 777 /app

WORKDIR /app

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install python-psycopg2

RUN pip install .

EXPOSE 5000

#CMD tail -f /dev/null
CMD ["gunicorn", "-b :5000", "selfservice_api:create_app()"]