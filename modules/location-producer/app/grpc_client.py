import grpc
import location_pb2
import location_pb2_grpc

print("Sending Location")

channel = grpc.insecure_channel("localhost:5007")
stub = location_pb2_grpc.LocationServiceStub(channel)

location1 = location_pb2.LocationMessage(
    person_id=40,
    latitude=-200,
    longitude=35
)

location2 = location_pb2.LocationMessage(
    person_id=9,
    latitude=-105,
    longitude=300
)

response1 = stub.Create(location1)
response2 = stub.Create(location2)

print("Sent User Locations")
print(location1, location2)