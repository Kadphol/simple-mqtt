from socket import *
import sys

SERV_PORT = 50000

while True:
    textout = sys.stdin.readline().strip()
    publish = textout.split()

    if(textout == 'exit'):
        break
    elif(len(publish) == 4):
        if(publish[0] == 'publish'):
            address = (publish[1], SERV_PORT)
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect(address)
                s.send(textout.encode('utf-8'))
            except:
                print('Invalid IP address')
        else:
            print('Invalid command!')
    else:
        print('Invalid argument')

s.close()