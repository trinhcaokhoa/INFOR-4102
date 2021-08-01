from socket import *


# main program
if __name__ == '__main__':
    # Set the connecttion
    serverName = 'localhost'
    serverPort = 12000


    
    for i in range(20):
        message = 'Ping massage number: ' + str(i)
        attempt = 0
        while attempt <=10: 
            client_socket = socket (AF_INET,SOCK_DGRAM)
            client_socket.settimeout(1.0)
            client_socket.sendto(message.encode(), (serverName, serverPort))
            print('Sent: ',message)
            try:
                modifiedMessage, serverAddress = client_socket.recvfrom(2048)
                print('Received: ', modifiedMessage.decode(),)
                client_socket.close()
                break
            except:
                print('Time Out')
                client_socket.close()
                attempt += 1
                condition = False
            
                
           
                
                

                
    
