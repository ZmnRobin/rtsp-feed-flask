FROM alpine3.12

RUN apt-get update

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

COPY . /app


EXPOSE 5002
CMD ["python3", "app.py"]