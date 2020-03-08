# simple-mqtt
1.type 'python3 broker.py' to run Broker program. <br />

2.type 'python3 subscriber.py' to run Subscriber program. <br />
  - 2.1 type 'subscribe <broker_ip_address> '<topic_name>'' to subscribe the topic <br />
    ex. subscribe 127.0.0.1 '/room1/light' <br />
    
3.type 'python3 publisher.py' to run Publisher program. <br />
  - 3.1 type 'publish <broker_ip_address> '<topic_name>' '<value>' to publish value of the topic <br />
    ex. publish 127.0.0.1 '/room1/light' 'value=on' <br />
  
4.See data in Broker terminal and subscriber terminal that subscribe to that topic <br />

5.exit program <br />
  - 5.1 On Publisher terminal press 'ctrl + c' or type 'exit' to exit publisher program. <br />
  - 5.2 On Subscriber terminal press 'ctrl + c' to exit subscriber program and remove socket in broker topics. <br />
  - 5.3 On Broker terminal press 'ctrl + c' to exit broker and subscriber program and shut down all socket that subsriber connected. <br />
