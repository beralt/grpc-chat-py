from concurrent import futures
from greet_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server
from greet_pb2 import HelloRequest, HelloReply
import grpc
import logging


class Service(GreeterServicer):
    def __init__(self):
        pass

    def SayHello(self, request: HelloRequest, context) -> HelloReply:
        reply = HelloReply()
        reply.message = f"Hello to you {request.name}!"
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_GreeterServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:5556")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    serve()
