# simple-mqtt
1.type 'python3 broker.py' to run Broker program.
2.type 'python3 subscriber.py' to run Subscriber program.
  2.1 type 'subscribe <broker_ip_address> '<topic_name>'' to subscribe the topic
    ex. subscribe 127.0.0.1 '/room1/light'
3.type 'python3 publisher.py' to run Publisher program.
  3.1 type 'publish <broker_ip_address> '<topic_name>' '<value>' to publish value of the topic
    ex. publish 127.0.0.1 '/room1/light' 'value=on'
4.See data in Broker terminal and subscriber terminal that subscribe to that topic
5.exit program
  5.1 On Publisher terminal press 'ctrl + c' or type 'exit' to exit publisher program.
  5.2 On Subscriber terminal press 'ctrl + c' to exit subscriber program and remove socket in broker topics.
  5.3 On Broker terminal press 'ctrl + c' to exit broker and subscriber program and shut down all socket that subsriber connected.
