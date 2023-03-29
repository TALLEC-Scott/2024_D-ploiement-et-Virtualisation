FROM python:3.10-slim-buster

WORKDIR /app
COPY sources /app
RUN apt-get update && apt-get -y install wget unzip libgl1 libglib2.0-0 && pip install --upgrade --no-cache-dir -r requirements.txt

RUN useradd -ms /bin/bash appuser
RUN chown -R appuser:appuser /app

USER appuser

RUN wget https://www.lrde.epita.fr/~jchazalo/SHARE/pero-printed_modern-public-2022-11-18.zip && unzip pero-printed_modern-public-2022-11-18.zip && rm *.zip
EXPOSE 8000

CMD ["uvicorn", "ocr_api:app", "--host", "0.0.0.0", "--port", "8000"]
