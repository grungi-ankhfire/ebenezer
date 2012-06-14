import socket
import threading

class EbenezerServer:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((socket.gethostname(), 42512))
        self.socket.listen(5)

    def run(self):
        while 1:
            (clientsocket, address) = self.socket.accept()
            print "Connection opened with ", address
            print clientsocket.recv(100)
            clientsocket.send( "Green-eyed monster.")
            clientsocket.close()

