from grpc_tools import protoc
from pathlib import Path

topdir = Path(__file__).parent

protosdir = topdir / "protos"

protofiles = [
    str(topdir / "protos" / "greet.proto"),
    str(topdir / "protos" / "chat.proto"),
]

for protofile in protofiles:
    protoc.main((
        "",
        f"-I{protosdir}",
        f"--python_out={topdir}",
        f"--grpc_python_out={topdir}",
        protofile
    ))