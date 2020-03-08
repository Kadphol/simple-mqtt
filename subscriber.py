from socket import *
import sys
import shlex

MAX_BUF = 2048
SERV_PORT = 50000

def shutdown():
    s.send(('subscribe quit').encode('utf-8'))
    s.close()

def main():
    while True:
        line = sys.stdin.readline().strip()
        subscribe = shlex.split(line)

        if(line == 'exit'):
            break
        elif(len(subscribe) == 3):
            if(subscribe[0] == 'subscribe'):
                address = (subscribe[1], SERV_PORT)
                try:
                    s.connect(address)
                    s.settimeout(None)
                    s.send(line.encode('utf-8'))
                    try:
                        while True:
                            txtin = s.recv(2048)
                            print('> %s' %txtin.decode('utf-8'))
                            if((txtin.decode('utf-8')) == 'QUIT'):
                                print('Broker is closed.')
                                try:
                                    sys.exit(0)
                                except SystemExit:
                                    os._exit(0)
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

if __name__ == '__main__':
    try:
        s = socket(AF_INET, SOCK_STREAM)
        main()
    except KeyboardInterrupt:
        print('')
        shutdown()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)