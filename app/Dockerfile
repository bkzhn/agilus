FROM python:3.11.4-slim

# RUN apt update && apt upgrade

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python", "run.py"]