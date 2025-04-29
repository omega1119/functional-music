FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./app /app/app
COPY ./config /app/config

CMD ["python", "app/main.py"]