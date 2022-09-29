import grpc

from greet_pb2_grpc import GreeterStub
from greet_pb2 import HelloRequest, HelloReply

from chat_pb2_grpc import ChatStub
from chat_pb2 import ChatMessage

# a simple generator for messages
def create_messages():
    msgs = [
        "can",
        "I",
        "haz",
        "msgs",
        "plz",
        "k",
        "thnx",
        "bye"
    ]
    for m in msgs:
        msg = ChatMessage()
        msg.message = m
        yield msg

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:5556") as channel:
        stub = GreeterStub(channel)
        request = HelloRequest()
        request.name = "Botty"
        response: HelloReply = stub.SayHello(request)
        print(response.message)

        chat_stub = ChatStub(channel)
        responses = chat_stub.ChitChat(create_messages())
        for response in responses:
            print(f"got msg back: {response.message}")