import time
from pinger_thread import Pinger_Thread


key = {} #place your google domain token


conf = []
with open('config_file.txt') as config_file:
    for line in config_file:
        conf.append(line.rstrip())

host_name = conf[0]

for ip in conf[1:]:
    pinger_agent = Pinger_Thread(ip, key,
                                 'place url for Google Sheet, you want messages to be parsed',
                                 'pinger', host_name)
    pinger_agent.start()
    time.sleep(2)
