## James Ortiz-Luis, 32386064
## Mario Ruiz, 46301389
## mail.py

from socket import *


msg = 'I love computer networks!\r\n'
endmsg = '.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'localhost'
portnumber = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, portnumber))
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
clientSocket.send('MAIL FROM: <athina@uci.edu>\r\n')
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '250':
    print '250 reply not received from server.'

# Send RCPT TO command and print server response.
clientSocket.send('RCPT TO: <jortizlu@uci.edu>\r\n')
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '250':
    print '250 reply not received from server.'

# Send DATA command and print server response.
clientSocket.send('DATA\r\n')
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '354':
    print '354 reply not received from server.'

# Send message data.
clientSocket.send(msg)

# Message ends with a single period.
clientSocket.send(endmsg)
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '250':
    print '250 reply not received from server.'

# Send QUIT command and get server response.
clientSocket.send('QUIT\r\n')
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '221':
    print '221 reply not received from server.'
    
clientSocket.close()

