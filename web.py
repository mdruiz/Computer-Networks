## James Ortiz-Luis, 32386064
## Mario Ruiz, 46301389
## web.py

#import socket module
from socket import *


serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
serverPort = 6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        if not message:
            continue
        else:
            filename = message.split()[1]
        print message
        if filename.endswith(".html"):
            f = open(filename[1:])
            outputdata = f.readlines()
        else:
            f = open(filename[1:], 'rb')
            outputdata = f.read()

        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\n\n')
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\n\n')
        #Close client socket
        connectionSocket.close()

serverSocket.close()
