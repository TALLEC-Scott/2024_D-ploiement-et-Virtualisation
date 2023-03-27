FROM python:3.10-slim-buster
WORKDIR /app

COPY . /app
RUN useradd -ms /bin/bash appuser
RUN chown -R appuser:appuser /app


RUN pip install --upgrade --no-cache-dir -r sources/requirements.txt

USER appuser
EXPOSE 8000
CMD ["uvicorn", "sources.main:app", "--host", "0.0.0.0", "--port", "8000"]
