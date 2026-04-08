FROM python:3.10

WORKDIR /app

COPY . .

CMD python inference.py && tail -f /dev/null
