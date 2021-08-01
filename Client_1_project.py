from socket import *


# main program
if __name__ == '__main__':
    # Set the connecttion
    serverName = 'localhost'
    serverPort = 48000
    av = 0
    for i in range(20):
        message = 'Ping massage number: ' + str(i)
        attempt = 0
        print('Sending : ',message)
        while attempt <=10: 
            print('Attempt: '+ str(attempt))
            client_socket = socket (AF_INET,SOCK_DGRAM)
            client_socket.settimeout(1.0)
            client_socket.sendto(message.encode(), (serverName, serverPort))
            
            try:
                modifiedMessage, serverAddress = client_socket.recvfrom(2048)
                print('Received: ', modifiedMessage.decode(),)
                
                client_socket.close()
                break
            except:
                print('Time Out')
                attempt += 1
                client_socket.close()
        print('\n')   
        av += attempt
print('Average number of attempts: '+ str(av/20))
                
                
            
                
           
                
                

                
    
