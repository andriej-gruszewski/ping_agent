from pinger import Pinger
import threading
import time


class Pinger_Thread(threading.Thread):

    def __init__(self, ip, token, url, sheet_name, host_name):
        threading.Thread.__init__(self)
        self.pinger = Pinger(ip, token, url, sheet_name, host_name)

    def run(self):
        while True:
            self.pinger.run_ping()
            self.pinger.add_status_flag_to_gs()
            time.sleep(60)