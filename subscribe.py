from socket import *
import sys

SERV_PORT = 50000

while True:
    line = sys.stdin.readline().strip()
    subscribe = line.split()

    if(line == 'exit'):
        break
    elif(len(subscribe) == 3):
        if(subscribe[0] == 'subscribe'):
            address = (subscribe[1], SERV_PORT)
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect(address)
                s.send(line.encode('utf-8'))
                try:
                    while True:
                        txtin = s.recv(2048)
                        print('> %s' %txtin.decode('utf-8'))
                except:
                    print('disconnected')
                    break
            except:
                print('Invalid IP address!')
        else:
            print('Invalid command!')
    else:
        print('Invalid arguments!')

s.close()