#import the socket header
import socket

#await user input, then separate the different parts into
#    their own variables
while 1:
    my_input = raw_input('myclient ')
    my_input = my_input.split()

    if my_input[0] == 'exit' or my_input[0] == 'quit':
        break

    my_host = my_input[0]
    port_num = int(my_input[1])
    mthd = my_input[2]
    obj = my_input[3]

    #create the socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect to the specified server using the specified port
    my_socket.connect((my_host, port_num))

    #determine the type of request being made
    if mthd == 'GET':
        msg = 'GET /' + obj + ' HTTP/1.1\r\nHost: ' + my_host + '\r\n\r\n'
        my_socket.send(msg)
    elif mthd == 'PUT':
        msg = 'PUT /' + obj +' HTTP/1.1\r\nHost: ' + my_host + '\r\n\r\n'
        my_socket.send(msg)
        #this is where it should send a file to write to the disk,
        # but I couldn't figure it out

    else:
        print('error')
        break;

    #create an output variable and fill it with data,
    # finally printing to the terminal
    output = ''
    while 1:
        buf = my_socket.recv(4096)
        if not buf:
            break
        output += buf
    print output

    #close the socket
    my_socket.close()
