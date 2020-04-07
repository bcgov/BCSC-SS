FROM nginx
COPY jwks.json /usr/share/nginx/json/jwks.json
COPY jwks.nginx.conf.template /etc/nginx/conf.d
#RUN rm /etc/nginx/conf.d/default.conf
ENV JWKS_SERVER_PORT=80
ENV JWKS_SERVER_NAME=localhost
RUN envsubst < /etc/nginx/conf.d/jwks.nginx.conf.template > /etc/nginx/conf.d/default.conf 
