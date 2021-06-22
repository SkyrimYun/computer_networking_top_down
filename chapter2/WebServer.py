#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort=12002
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#Fill in end
while True:
 #Establish the connection
 print('Ready to serve...')
 connectionSocket, addr = serverSocket.accept()
 try:
    message =  connectionSocket.recv(1024)
    print('message: ', message)
    filename = message.split()[1][1:].decode()
    print('filename: ',filename)
    f = open('/home/yunfan/work_spaces/computer_networking_top_down/chapter2/'+filename)
    outputdata = f.read()
    #Send one HTTP header line into socket
    #Fill in start
    header='HTTP/1.1 200 OK\nConnection: close\nContent-TYpe: text/html\nContent-Length: %d\n\n' %(len(outputdata))
    connectionSocket.send(header.encode())
    #Fill in end
    #Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
    connectionSocket.close()
 except IOError:
  #Send response message for file not found
  #Fill in start
  header = 'HTTP/1.1 404 Not Found'
  connectionSocket.send(header.encode())
  #Fill in end
  #Close client socket
  #Fill in start
  connectionSocket.close()
  #Fill in end
serverSocket.close()
