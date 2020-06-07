
import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(socket.cryptohack.org, 11112)
def send(data):
    request = json.dumps(data).encode()
    tn.write(request)
def recv():
    line = readline()
    return json.loads(line.decode())

