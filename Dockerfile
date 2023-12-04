# Dockerfile to build production API with Gunicorn WSGI

FROM python:3.10

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /
WORKDIR /

EXPOSE 8000

CMD ["/bin/sh",  "-c",  "gunicorn -w 1 -b 0.0.0.0:8000 app:app"]