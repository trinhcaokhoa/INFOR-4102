import random
from time import sleep
from socket import *
BUSY_PERCENT = 50
serverPort = 48000
def get_busy():
    random_number = random.randint(0, 100)
    if random_number < BUSY_PERCENT:
        print("Getting busy ...")
        sleep(1)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive requests')
while True:
    try:
        get_busy()
        message, clientAddress = serverSocket.recvfrom(2048)
        print('Received request:\n', message.decode(), '\nfrom client:\n', clientAddress)
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(),clientAddress)
        print('Send: ',modifiedMessage)
        get_busy()
    except:
        continue
