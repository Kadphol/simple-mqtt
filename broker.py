from socket import * 
from threading import Thread
import traceback
import os,sys

SERV_PORT = 50000

topics = {}

def handle_client(s,addr):
    try:
        while True:
            txtin = s.recv(1024)
            value = txtin.decode('utf-8').split()

            if(value[0] == 'publish'):
                print('Publish> %s %s from %s:%s' %(value[2],value[3],str(addr[0]),str(addr[1])))
                for topic in topics:
                    if(topic == value[2]):
                        for subscriber in topics[value[2]]:
                            subscriber.send(txt[3].encode('utf-8'))
                s.close()
                break
            elif(value[0] == 'subscribe'):
                if(value[2] not in topics):
                    subscriber = []
                    subscriber.append(s)
                    topics[value[2]] = subscriber
                else:
                    topics[value[2]].append(s)
    except:
        for topic in topics:
            for subscriber in topics[topic]:
                if(subscriber == s):
                    topics[topic].remove(s)
        print('%s:%s disconnected' %(str(addr[0]),str(addr[1])))
    
    s.close()
    return

def main(argv):
    address = '127.0.0.1'
    if(len(sys.argv) == 2):
        address = str(sys.argv[1])
    addr = (address, SERV_PORT)
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(addr)
    s.listen(5)
    print ('Broker started at ' + address)

    while True:
        sckt, addr = s.accept()
        ip, port = str(addr[0]), str(addr[1]) 
        print ('New client connected from ' + ip + ':' + port)
    
        try:
            Thread(target=handle_client, args=(sckt,addr)).start()
        except:
            print("Cannot start thread..")  
            trackback.print_exc()
    s.close()

if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print ('Interrupted ..')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


