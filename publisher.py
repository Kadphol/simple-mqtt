from socket import *
import sys
import shlex

MAX_BUF = 2048
SERV_PORT = 50000

def main():
    while True:
        try:
            textout = sys.stdin.readline().strip() #read text from standard input
            publish = shlex.split(textout) #split text with shell lexical split

            if(textout == 'exit'): #exit
                break
            elif(len(publish) == 4): #check number of argument
                if(publish[0] == 'publish'): #check command
                    address = (publish[1], SERV_PORT) 
                    try:
                        s.connect(address) #connect socket
                        s.send(textout.encode('utf-8')) #send textout
                    except:
                        print('Invalid IP address')
                else:
                    print('Invalid command!')
            else:
                print('Invalid argument')
        except KeyboardInterrupt:
            print('')
            print('exit')
            break

    s.close()

if __name__ == '__main__':
    try:
        s = socket(AF_INET, SOCK_STREAM)
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)