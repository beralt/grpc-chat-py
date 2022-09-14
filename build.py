from grpc_tools import protoc
from pathlib import Path

topdir = Path(__file__).parent
protosdir = topdir / "protos"
protofile = topdir / "protos" / "greet.proto"

protoc.main((
    "",
    f"-I{protosdir}",
    f"--python_out={topdir}",
    f"--grpc_python_out={topdir}",
    str(protofile)
))