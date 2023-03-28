FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get -y install wget unzip libgl1 && pip install --upgrade --no-cache-dir -r sources/requirements.txt

RUN useradd -ms /bin/bash appuser
RUN chown -R appuser:appuser /app

USER appuser

RUN wget https://www.lrde.epita.fr/~jchazalo/SHARE/pero-printed_modern-public-2022-11-18.zip && unzip pero-printed_modern-public-2022-11-18.zip && rm *.zip


