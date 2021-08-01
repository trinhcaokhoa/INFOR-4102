# INFOR-4102
The project to describe Exponential backoff and Linear Backoff The goal of this project is to gain firsthand experience in understanding and comparing various backoff strategies.

Problem Statement The code below simulates a really busy server that accepts sentences as requests and returns capitalized sentences as responses. This code is also available as a text attachment, and must not be altered.

import random 
from time import sleep 
from socket import * 
BUSY_PERCENT = 50 
serverPort = 12000 
def get_busy(): random_number = random.randint(0, 100) 
if random_number < BUSY_PERCENT: print("Getting busy ...")
sleep(1) 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind((’’, serverPort)) 
print(’The server is ready to receive requests’)
while True: 
get_busy() 1 message, clientAddress = serverSocket.recvfrom(2048) 
print(’Received request:\n’, message.decode(), ’\nfrom client:\n’, clientAddress)
modifiedMessage = message.decode().upper() 
serverSocket.sendto(modifiedMessage.encode(), clientAddress) 
get_busy()

• After sending each message, the client waits up to 1 second for a response from the server. If a response is received within this time, it prints the response. Otherwise, it retries after a delay. Consider the following three delay strategies.

No delay. Retry happens immediately after timout.

Exponential backoff. The delay (measured in seconds) for attempt 0 is 0, for attempt 1 it is a random number selected from {0, 1}, for attempt 2 it is a random number selected from {0, 1, 2, 3}, for attempt 3 it is a random number selected from {0, 1, 2, 3, 4, 5, 6, 7}, and so on.

Linear backoff. the delay for attempt 0 is 0, for attempt 1 it is a random number selected from {0, 1}, for attempt 2 it is a random number selected from {0, 1, 2}, for attempt 3 it is a random number selected from {0, 1, 2, 3}, for attempt 4 it is a random number selected from {0, 1, 2, 3, 4} and so on. 

• In each case, if after 10 attempts the client still doesn’t get a response, it simply gives up that message and moves on to the next message. • At the end, the client prints out the average number of attempts per message. For each of the above three strategies, implement a client program. The attached file SampleOutput.txt shows what a sample run of this client should produce. Compare the average number of retries per message required for each strategy, and identify the best strategy
