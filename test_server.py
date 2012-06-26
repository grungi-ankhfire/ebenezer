from twisted.internet import protocol, reactor
from twisted.protocols import basic

class EbenezerProtocol(basic.LineReceiver):
    
    def __init__(self):
        self.state = "GETNAME"
        self.user = ""

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.user= line
            self.transport.write(self.factory.getUser(self.user)+"\r\n")
            self.state = "GOTNAME"
        else:
            self.transport.write("Exiting"+"\r\n")
            self.transport.loseConnection()

class EbenezerFactory(protocol.ServerFactory):

    protocol = EbenezerProtocol

    def __init__(self, **kwargs):
        self.connected_users = ["alice", "bob"]

    def getUser(self, user):
        if user in self.connected_users:
            return user
        else:
            return "No such user" 

reactor.listenTCP(42512, EbenezerFactory())
reactor.run()