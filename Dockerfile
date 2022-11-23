FROM python:3.10
RUN apt-get update && apt-get -y install netcat
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src ./
COPY ./docker-entrypoint.sh .
COPY ./env_files/python/.env .
EXPOSE 8000
