HOST = '<your_host>'
PORT = 1025
BUFSIZE = 4096

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.settimeout(3)

part1 = '5000 00 FF 03FF 00'
part2 = '0000'
part3 = '0000 1002 0000 0001'

part1 = part1.strip().replace(' ', '')
part2 = part2.strip().replace(' ', '')
part3 = part3.strip().replace(' ', '')

part3_length = len(part3.encode('ascii')).to_bytes(2, byteorder='big').hex().upper()

new_data = f'{part1}{part3_length}{part3}'

ascii_data = new_data.encode('ascii')

# send request
sock.send(ascii_data)

# response
res = sock.recv(BUFSIZE)
print(res)

sock.close()