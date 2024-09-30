FROM python:3.12

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DB_NAME="${DB_NAME}"
ENV DB_USER="${DB_USER}"
ENV DB_PASSWORD="${DB_PASSWORD}"
ENV DB_HOST="${DB_HOST}"
ENV DB_PORT="${DB_PORT}"
ENV FILE_PATH="${FILE_PATH}"

COPY run.sh /opt/app/run.sh
COPY requirements.txt /opt/app/requirements.txt

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

RUN chmod +x run.sh

ENTRYPOINT ["./run.sh"]