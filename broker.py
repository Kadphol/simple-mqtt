from socket import * 
from threading import Thread
import traceback
import os,sys
import shlex

MAX_BUF = 2048
SERV_PORT = 50000

topics = {}
 
def shutdown_socket(): #close socket in topics
    try:
        for sockets in topics.values():
            for s in sockets:
                s.send('QUIT'.encode('utf-8')) #send 'QUIT' message to all subscriber to shutdown.
    except:
        pass

def delete_socket(conn_sock): #remove socket in topics
    for sockets in topics.values():
        for s in sockets:
            if(s == conn_sock):
                del s

def add_socket(conn_sock, topic): #add socket to topics
    if(topic in topics):
        topics[topic].append({conn_sock}) #append socket to existing topic
    else:
        topics[topic] = {conn_sock} #add new topic 


def handle_client(conn_sock, cli_sock_addr): #handle client socket
    while True:
        txtin = conn_sock.recv(2048).decode('utf-8') #receive text for client and decode
        message = shlex.split(txtin) #split text with shell lexical split

        if(message[0] == 'subscribe'): #if this socket is subscribe
            if(message[1] == 'quit'): #if subscribe is quit
                print('%s:%s disconneted' %(cli_sock_addr[0],cli_sock_addr[1]))
                delete_socket(conn_sock) #delete socket in topics
                break
            else:
                print('%s:%s subscribe for topic %s' %(cli_sock_addr[0],cli_sock_addr[1],message[2]))
                add_socket(conn_sock,message[2]) #add socket to topic

        elif(message[0] == 'publish'):
            if(message[2] in topics.keys()):
                for s in topics[message[2]]:
                    s.send(message[3].encode('utf-8')) #publish value to subscriber in that topic
            print('%s:%s disconnected' %(cli_sock_addr[0],cli_sock_addr[1]))
            conn_sock.close() #close socket
            break



def main():
    serv_sock_addr = ('127.0.0.1', SERV_PORT) #broker address
    welcome_sock.bind(serv_sock_addr) #bind welcome socket with address
    welcome_sock.listen(5) #enable to 5 connections for max
    print ('Broker started at %s' %serv_sock_addr[0])

    while True:
        conn_sock, cli_sock_addr = welcome_sock.accept() #accept connection socket for new connection
        ip, port = str(cli_sock_addr[0]), str(cli_sock_addr[1]) 
        print ('New client connected from ' + ip + ':' + port)
    
        try:
            Thread(target=handle_client, args=(conn_sock, cli_sock_addr)).start() #start thread server
        except:
            print("Cannot start thread..")
            trackback.print_exc()   


if __name__ == '__main__':
    try:
        welcome_sock = socket(AF_INET, SOCK_STREAM) #open welcome socket
        main()
    except KeyboardInterrupt:
        shutdown_socket() #close all socket after shutdown broker
        print('')
        print('Shut down socket')
        welcome_sock.close() #close welcome socket
        print('Broker shutdown')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)