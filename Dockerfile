FROM python:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requeriments.txt


EXPOSE 90

CMD [ "python", "main.py" ]