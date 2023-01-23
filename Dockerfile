FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requriments.txt .

RUN pip install --upgrade pip
RUN pip install -r requriments.txt


COPY . .
