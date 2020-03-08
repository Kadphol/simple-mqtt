from socket import *
import sys
import shlex

MAX_BUF = 2048
SERV_PORT = 50000

def check_argument(subscribe): #check argument of command
    if(len(subscribe) == 3):
        if(subscribe[0] == 'subscribe'):
            return True
        else:
            print('Invalid command')
            return False
    else:
        print('Invalid argument')
        return False

def shutdown_socket(s): #close socket and send message to broker to remove socket
    text = 'subscribe quit'
    s.send(text.encode('utf-8'))
    s.close()

def main():
    while True:
        line = sys.stdin.readline().strip() #read text from standard input
        subscribe = shlex.split(line) #split text with shell lexical split

        if(check_argument(subscribe)): #check argument
            address = (subscribe[1], SERV_PORT) #address
            s.connect(address) #connect socket
            s.settimeout(None)
            s.send(line.encode('utf-8')) #send message to broker
            try:
                while True:
                    txtin = s.recv(2048) #recv message from broker
                    if(txtin.decode('utf-8') == 'QUIT'):
                        print('Broker is closed') #if broker is closed
                        s.close()
                        try:
                            sys.exit(0)
                        except SystemExit:
                            os._exit(0)
                    else:
                        print('> %s' %txtin.decode('utf-8')) #print value message for subscribed topic
            except:
                print('\ndisconnected')
                break
        else:
            pass
    shutdown_socket(s) #shutdown socket

if __name__ == '__main__':
    try:
        s = socket(AF_INET, SOCK_STREAM) #create socket
        main()
    except KeyboardInterrupt:
        shutdown_socket(s)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)