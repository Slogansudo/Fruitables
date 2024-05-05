FROM python:3.10.12-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /app

COPY requirement.txt requirement.txt

RUN pip install --upgrade pip
RUN pip install -r requirement.txt

COPY . .