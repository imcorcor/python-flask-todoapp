FROM tiangolo/meinheld-gunicorn-flask

WORKDIR /app

RUN mkdir models static templates

COPY ./models models

COPY ./static static

COPY ./templates templates

COPY create_database.py .

COPY main.py .

ENV APP_VERSION=1.2.3.4

EXPOSE 5000

RUN python3 create_database.py

CMD [ "python3", "main.py" ]