
# -*- coding : utf-8 -*-
import socket
import ssl

from urllib.parse import quote_plus

request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: Foundations of Python Network Programming example search4.py\r\n\
Connection: close\r\n\
\r\n\
"""


def geocode(address):
    #Create a new socket using the given address family,
    #socket type and protool number.
    unencrypted_sock = socket.socket()
    #Connect to a remote socket at address 
    unencrypted_sock.connect(('nominatim.openstreetmap.org',443))
    #ssl: TLS/SSL wrapper for socket objects
    #Takes an instance sock of socket.socket,and return an instance of ssl.SSLsocket
    sock = ssl.wrap_socket(unencrypted_sock)
    #print(quote_plus(address))
    request = request_text.format(quote_plus(address))
    #print(request)
    sock.sendall(request.encode('ascii'))
    #print(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))


if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')








