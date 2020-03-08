from socket import *
import sys
import shlex

MAX_BUF = 2048
SERV_PORT = 50000

def main():
    while True:
        textout = sys.stdin.readline().strip()
        publish = shlex.split(textout)

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

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)