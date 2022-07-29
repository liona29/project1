FROM python:3.10.5-slim-buster

RUN pip install flask
# RUN pip install psycopg2
# RUN pip install psycopg2==2.7.5 --ignore-installed

# WORKDIR ./
COPY . .

CMD ["python", "./app.py"]
