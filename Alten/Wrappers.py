from PySide6.QtCore import QObject, Property, Signal, Slot

import grpc
from greet_pb2_grpc import GreeterStub
from greet_pb2 import HelloRequest, HelloReply

import logging

logger = logging.getLogger(__name__)


class Greeter(QObject):
    def __init__(self, channel: grpc.Channel, parent: QObject = None):
        super().__init__(parent=parent)
        self._response: str = ""
        self._stub = GreeterStub(channel)

    responseChanged = Signal()

    @Property(str, notify=responseChanged)
    def response(self) -> str:
        return self._response

    @Slot(str)
    def greet(self, name: str) -> None:
        logger.debug(f"Trying to send greeting")
        request = HelloRequest()
        request.name = name
        request_future = self._stub.SayHello.future(request)
        request_future.add_done_callback(self._done)

    def _done(self, future: grpc.Future) -> None:
        logger.debug(f"Done greeting")
        reply: HelloReply = future.result()
        self._response = reply.message
        self.responseChanged.emit()
