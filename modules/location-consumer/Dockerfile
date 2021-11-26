FROM python:3.8

WORKDIR .
COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
ENV DB_USERNAME=ct_geoconnections
ENV DB_PASSWORD=d293aW1zb3NlY3VyZQ==
ENV DB_NAME=geoconnections
ENV DB_HOST=postgres-geoconnections
ENV DB_PORT=5432
ENV KAFKA_URL =  kafka-service:9092
ENV KAFKA_TOPIC = locations

EXPOSE 5008

CMD [ "python", "app/connect.py" ]