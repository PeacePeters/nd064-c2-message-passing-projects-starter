FROM python:3.8

WORKDIR .
COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -Iapp --python_out=. --grpc_python_out=. app/location.proto
ENV KAFKA_URL =  kafka-service:9092
ENV KAFKA_TOPIC = locations

EXPOSE 5007

CMD [ "python", "app/grpc_server.py" ]