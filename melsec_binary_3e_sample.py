HOST = '<your_host>' 
PORT = 1025
BUFSIZE = 4096

import socket

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.settimeout(3)

# UDP
# UDP_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
# UDP_client.settimeout(10)
# UDP_client.connect((host, port))

data = [
    0x50,0x00,      # Subheader
    0x00,           # network No.
    0xFF,           # station No.
    0xFF,0x03,      # module I/O No.
    0x00,           # multidrop station No.
    0x00,0x00,      # length 
    0x04,0x00,      # Monitoring timer
    0x02,0x10,      # Command
    0x00,0x00,      # Subcommand
    0x01,0x00
]

# length
data[7] = len(data[9:]) & 0xFF
data[8] = (len(data[9:]) >> 16) & 0xFF

# send request
sock.send(bytes(data))

# response
res = sock.recv(BUFSIZE)
print(res.hex())

sock.close()