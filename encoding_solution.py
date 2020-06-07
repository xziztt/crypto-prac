from pwn import * # pip install pwntools
import json
import string
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes



r = remote('socket.cryptohack.org', 13377, level = 'debug')
def json_recv():
        line = r.recvline()
        return json.loads(line.decode())

def json_send(hsh):
        request = json.dumps(hsh).encode()
        r.sendline(request)


for i in range(0,101):
    
    received = json_recv()
    print("yes2")

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])


    if received["type"] == "base64":
                finaltemp = base64.b64decode(received["encoded"]).decode('utf-8')
                finaltemp2 = str(finaltemp)
                finaltemp2.replace("'","")
                final = finaltemp2
                print("yes")
    elif received["type"] == "hex":
                final = bytearray.fromhex(received["encoded"]).decode()
                print("yes")
    elif received["type"] == "rot13":
                final = codecs.decode(received["encoded"], 'rot_13')
                print("yes")
    elif received["type"] == "bigint":
                hex_int = int(received["encoded"], 16)
                finaltemp = format(hex_int,'x')
                final = bytearray.fromhex(finaltemp).decode()
                
                print("yes")
    elif received["type"] == "utf-8":
                finaltemp = [chr(b) for b in received["encoded"]]
                str1 = ""
                for i in finaltemp:
                    str1 += i
                final = str1
                print("yes")
    print(final)

    to_send = {
        "decoded": final
    }
    json_send(to_send)
        
