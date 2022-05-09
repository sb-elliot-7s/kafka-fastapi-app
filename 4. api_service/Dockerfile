FROM python:3.9

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./app /app

ENV HOST 0.0.0.0

ENV PORT 8000

CMD uvicorn main:app --reload --host $HOST --port $PORT
