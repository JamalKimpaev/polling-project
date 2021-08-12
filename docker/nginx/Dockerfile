FROM nginx:stable as dev
RUN apt-get update && apt-get install openssl -y
ARG NGINX_HOST
ENV NGINX_HOST ${NGINX_HOST}
ARG ALLOW_ACCESS=deny
ENV ALLOW_ACCESS ${ALLOW_ACCESS}
ADD docker/nginx/*.template /build/
RUN envsubst < /build/dev.template > /etc/nginx/conf.d/default.conf

FROM nginx:stable as prod
COPY --from=dev /etc/nginx/conf.d/prod.conf.disabled /etc/nginx/conf.d/default.conf
COPY --from=polling-system-project_back:latest /project/static/ /back/static/
