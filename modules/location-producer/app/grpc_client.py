import grpc
import location_pb2
import location_pb2_grpc

channel = grpc.insecure_channel("localhost:5008")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    longitude=-105.5719566,
    latitude=35.0585126,
    person_id=9
)

response = stub.Create(location)
print(response)