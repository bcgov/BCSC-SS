# build stage
FROM public.ecr.aws/bitnami/node:12-prod as build-stage

# Using arguments to make it available in build
ARG API_BASE_URL
ARG KEYCLOAK_URL
ARG KEYCLOAK_REALM
ARG KEYCLOAK_CLIENT
ARG ENABLE_BETA

ENV VUE_APP_API_BASE_URL=${API_BASE_URL}
ENV VUE_APP_KEYCLOAK_URL=${KEYCLOAK_URL}
ENV VUE_APP_KEYCLOAK_REALM=${KEYCLOAK_REALM}
ENV VUE_APP_KEYCLOAK_CLIENT=${KEYCLOAK_CLIENT}
ENV VUE_APP_ENABLE_BETA=${ENABLE_BETA}

WORKDIR /src
COPY package*.json ./
RUN npm install
COPY . .

RUN npm run build

# production stage
FROM public.ecr.aws/bitnami/nginx:1.18 as production-stage

COPY --from=build-stage /src/dist /app
COPY --from=build-stage /src/nginx.conf /opt/bitnami/nginx/conf/server_blocks/bcsc-ss-ui.conf

EXPOSE 8080

ENTRYPOINT [ "/opt/bitnami/scripts/nginx/entrypoint.sh" ]
CMD [ "/opt/bitnami/scripts/nginx/run.sh" ]
