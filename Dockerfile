FROM python:3.11.6-slim-bullseye as libs

COPY ./src/requirements.txt .

RUN pip install -r requirements.txt

FROM python:3.11.6-slim-bullseye

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends curl \
    && update-ca-certificates

EXPOSE 5060

WORKDIR /app

COPY ./src/log_config.yaml /app/log_config.yaml

COPY --from=libs /usr/local /usr/local
COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]