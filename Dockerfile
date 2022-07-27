FROM python:3.10.5-slim-buster

RUN pip install flask

WORKDIR /home/ari/k8s/project1/flaskexample/
COPY ./flask .

CMD ["python", "./app.py"]