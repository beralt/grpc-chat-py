# Python implementation of the gRPC chat server

## Building and setup

The steps are

1. Download Python 3.7+ from (python.org)[https://python.org]
2. (Create a venv and activate it)
3. Use `requirements.txt` to satisfy depencencies using `pip install -r requirements.txt`
4. Generate the gRPC sources using `python build.py`
5. Start server, client CLI or client GUI using `python server.py`, `python client_cli.py` or `python client_gui.py`