# pull official base image
FROM python:3.9.5-alpine
LABEL maintainer=uddipta
# set work directory
WORKDIR /calculator
ADD requirements.txt /calculator

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies required for psycopg2 python package
RUN apk update && apk add libpq
RUN apk update && apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy entrypoint.sh
ADD entrypoint.sh /calculator

# copy project
ADD . /calculator

# run entrypoint.sh
#ENTRYPOINT ["/calculator/entrypoint.sh"]
