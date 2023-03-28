FROM python:3.10-slim-buster
WORKDIR /app

COPY . /app
RUN useradd -ms /bin/bash appuser
RUN chown -R appuser:appuser /app

RUN pip install --upgrade --no-cache-dir -r sources/requirements.txt
USER appuser
RUN apt-get install unzip && wget https://www.lrde.epita.fr/~jchazalo/SHARE/pero-printed_modern-public-2022-11-18.zip && unzip pero-printed_modern-public-2022-11-18.zip && rm *.zip

CMD [python, test_ocr.py]
