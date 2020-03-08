from socket import * 
from threading import Thread
import traceback
import os,sys
import shlex

MAX_BUF = 2048
SERV_PORT = 50000

topics = {}
 
def shutdown_socket():
    for sockets in topics.values():
        for s in sockets:
            s.send('QUIT'.encode('utf-8'))

def delete_socket(conn_sock):
    for sockets in topics.values():
        for s in sockets:
            if(s == conn_sock):
                sockets.remove(conn_sock)

def add_socket(conn_sock, topic):
    if(topic in topics):
        topics[topic].append({conn_sock})
    else:
        topics[topic] = {conn_sock}


def handle_client(conn_sock, cli_sock_addr):
  while True:
    try:
        txtin = conn_sock.recv(2048).decode('utf-8')
        message = shlex.split(txtin)

        if(message[0] == 'subscribe'):
            if(message[1] == 'quit'):
                print('%s:%s disconneted' %(cli_sock_addr[0],cli_sock_addr[1]))
                delete_socket(conn_sock)
                break
            else:
                print('%s:%s subscribe for topic %s' %(cli_sock_addr[0],cli_sock_addr[1],message[2]))
                add_socket(conn_sock,message[2])

        elif(message[0] == 'publish'):
            if(message[2] in topics.keys()):
                for s in topics[message[2]]:
                    s.send(message[3].encode('utf-8'))
            conn_sock.close()
        break
    except BlockingIOError:
        pass


def main():
    serv_sock_addr = ('127.0.0.1', SERV_PORT)
    welcome_sock.bind(serv_sock_addr)
    welcome_sock.listen(5)
    print ('Broker started at %s' %serv_sock_addr[0])

    while True:
        conn_sock, cli_sock_addr = welcome_sock.accept()
        ip, port = str(cli_sock_addr[0]), str(cli_sock_addr[1]) 
        print ('New client connected from ' + ip + ':' + port)
    
        try:
            Thread(target=handle_client, args=(conn_sock, cli_sock_addr)).start()
        except:
            print("Cannot start thread..")
            trackback.print_exc()   


if __name__ == '__main__':
    try:
        welcome_sock = socket(AF_INET, SOCK_STREAM)
        main()
    except KeyboardInterrupt:
        shutdown_socket()
        print('')
        print('Shut down socket')
        welcome_sock.close()
        print('Broker shutdown')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)