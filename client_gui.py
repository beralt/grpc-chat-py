from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterSingletonInstance

import grpc
import pathlib
import sys
import logging
from Alten.Wrappers import Greeter

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qml_file = pathlib.Path(__file__).parent / "qml" / "main.qml"
    url = QUrl.fromLocalFile(qml_file)

    # setup the greeter and expose it to QML as a singleton
    channel = grpc.insecure_channel("localhost:5556")
    greeter = Greeter(channel)
    qmlRegisterSingletonInstance(Greeter, "Alten", 1, 0, "Greeter", greeter)

    engine.load(url)

    # check if the above file was indeed loaded
    if not engine.rootObjects():
        logger.error(f"Failed to load {qml_file}")
        sys.exit(-1)

    # starts the event loop
    res = app.exec()

    channel.close()

    sys.exit(res)
