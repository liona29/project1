FROM python:3.10.5-slim-buster

RUN pip install flask

WORKDIR ./flask/
COPY . .

CMD ["python", "./app.py"]
