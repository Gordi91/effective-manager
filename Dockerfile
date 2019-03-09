FROM python:3.7-alpine
MAINTAINER Szymon Pecuch

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /effective_manager
WORKDIR /effective_manager
COPY ./effective_manager /effective_manager

RUN adduser -D user
USER user

