FROM python:latest

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]