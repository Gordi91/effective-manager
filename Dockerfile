FROM python:3.7-alpine
MAINTAINER Szymon Pecuch

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirements.txt
RUN apk add --update wkhtmltopdf
RUN apk del .tmp-build-deps

RUN mkdir /effective_manager
WORKDIR /effective_manager
COPY ./effective_manager ./effective_manager

RUN mkdir -p ./vol/web/media
RUN mkdir -p ./vol/web/static
RUN adduser -D user
RUN chown -R user:user ./vol/
RUN chmod -R 755 ./vol/web
USER user