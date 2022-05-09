FROM python:3.9

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./app /app

CMD faust -A main worker -l info

