from socket import *
import random
import time

# Function to delay the client side
def delay(num_of_tries):
    if num_of_tries > 0:
        delay_time = random.randint(0,num_of_tries)
        print('Entering delay '+ str(delay_time))
        time.sleep(delay_time)
    else:
        pass    



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
            delay(attempt)
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
                
            
                
           
                
                

                
    
