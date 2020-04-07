FROM nginx:stable
# support running as arbitrary user which belogs to the root group
RUN chmod g+rwx /var/cache/nginx /var/run /var/log/nginx
# users are not allowed to listen on priviliged ports
RUN sed -i.bak 's/listen\(.*\)80;/listen 8081;/' /etc/nginx/conf.d/default.conf
EXPOSE 8081
# comment user directive as master process is run as user in OpenShift anyhow
RUN sed -i.bak 's/^user/#user/' /etc/nginx/nginx.conf
COPY jwks.json /usr/share/nginx/json/jwks.json
COPY jwks.nginx.conf.template /etc/nginx/conf.d
ENV JWKS_SERVER_PORT=8081
ENV JWKS_SERVER_NAME=localhost

RUN envsubst < /etc/nginx/conf.d/jwks.nginx.conf.template > /etc/nginx/conf.d/default.conf