from concurrent import futures

from greet_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server
from greet_pb2 import HelloRequest, HelloReply

from chat_pb2_grpc import ChatServicer, add_ChatServicer_to_server
from chat_pb2 import ChatMessage

import grpc
import logging


class Service(GreeterServicer):
    def __init__(self):
        pass

    def SayHello(self, request: HelloRequest, context) -> HelloReply:
        reply = HelloReply()
        reply.message = f"Hello to you {request.name}!"
        return reply

class ChatService(ChatServicer):
    def __init__(self) -> None:
        pass

    def ChitChat(self, request_iterator, context):
        for new_message in request_iterator:
            msg = ChatMessage()
            msg.message = f"Did you just say '{new_message.message}'?"
            yield msg


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Service(), server)
    add_ChatServicer_to_server(ChatService(), server)
    server.add_insecure_port("[::]:5556")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    serve()
