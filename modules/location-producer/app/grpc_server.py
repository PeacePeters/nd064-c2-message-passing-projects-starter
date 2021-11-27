from concurrent import futures
import grpc
import time
import json
import os
import location_pb2
import location_pb2_grpc
from kafka import KafkaProducer


kafka_url = os.environ["KAFKA_URL"]
kafka_topic = os.environ["KAFKA_TOPIC"]
kafka_producer = KafkaProducer(bootstrap_servers=kafka_url)
class LocationServicer(location_pb2_grpc.LocationServiceServicer):

    def __init__(self, *args, **kwargs):
        pass

    def Create(self, request, context):

        request_value = {
            "person_id": int(request.person_id),
            "latitude": float(request.latitude),
            "longitude": float(request.longitude)
        }
        print(f'Location created - gRPC:  {request_value}')

        kafka_request = json.dumps(request_value, indent=2).encode('utf-8')
        kafka_producer.send(kafka_topic, kafka_request)
        kafka_producer.flush()
        return location_pb2.LocationMessage(**request_value)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
    server.add_insecure_port('[::]:5007')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()