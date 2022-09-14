import grpc
from greet_pb2_grpc import GreeterStub
from greet_pb2 import HelloRequest, HelloReply

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:5556") as channel:
        stub = GreeterStub(channel)
        request = HelloRequest()
        request.name = "Botty"
        response: HelloReply = stub.SayHello(request)
        print(response.message)
