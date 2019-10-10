#import socket and regular expression headers
import socket
import re

#the user sets the port number
my_port = raw_input('myserver')


#create the socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sets the socket options
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#binds the port to the localhost
my_socket.bind(('',int(my_port)))
#only one connection is allowed at a time
my_socket.listen(1)
print('The server is ready to receive')
while True:
    #connect to a clinet, and receive its message
    my_connection, addr = my_socket.accept()
    msg = my_connection.recv(1024)

    #use regular expressions to figure out what kind of
    #  request was received
    match_get = re.match('GET', msg)
    match_put = re.match('PUT', msg)

    if(match_get):
        #acknowledge GET request and grab the index file
        my_connection.sendall("HTTP/1.1 200 OK\n")
        my_file = "index.html"

        #open the file in 'read binary' mode
        my_file_object = open(my_file, 'rb')

        #begin sending the clinet the index.html file
        my_data = my_file_object.read(256)
        while(my_data):
            my_connection.send(my_data)
            my_data = my_file_object.read(256)
        my_file_object.close()

    elif(match_put):
        #acknowledge the PUT request
        my_connection.sendall("HTTP/1.1 200 OK File Created")
        #this is where it should write to disk, but I
        # couldn't figure out how to do it

    #close the connection
    my_connection.close()
