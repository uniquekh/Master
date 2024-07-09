FROM python:3.9.7-slim-buster

WORKDIR .
COPY . .

RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg aria2 \
    && pip install --no-cache-dir -r requirements.txt
CMD gunicorn app:app & python3 main.py
