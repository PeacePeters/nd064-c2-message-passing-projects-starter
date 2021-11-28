import grpc
import location_pb2
import location_pb2_grpc

print("Sending location...")

channel = grpc.insecure_channel("localhost:5007")
stub = location_pb2_grpc.LocationServiceStub(channel)

location1 = location_pb2.LocationMessage(
    person_id=40,
    latitude=-200.553638,
    longitude=35.794572
)

location2 = location_pb2.LocationMessage(
    person_id=15,
    latitude=-105.337645,
    longitude=300.892675
)

response1 = stub.Create(location1)
response2 = stub.Create(location2)
print(location1, location2)