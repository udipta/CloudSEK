FROM nginx:1.19.0-alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY calculator.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/calculator.conf /etc/nginx/sites-enabled/ \
    && rm /etc/nginx/conf.d/default.conf