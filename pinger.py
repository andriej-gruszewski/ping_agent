import platform
import os
import subprocess
from datetime import datetime
from gsp_parser import GSP_Parser

class Pinger:

    def __init__(self, ip, token, url, sheet_name, host_name):
        self.ip = ip
        self.status = ['UP']
        self.parser = GSP_Parser(token, url, sheet_name)
        self.host_name = host_name

    def run_ping(self):
        ip = self.ip
        # Option for the number of packets as a function
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        # Building the command
        command = f'ping {ip} {param} 4'
        msg = os.popen(command)
        result = msg.readlines()
        # Assigning ping command status of IP adress
        if len(result) == 11:
            self.status.append('UP')
        else:
            self.status.append('DOWN')
        return self.status

    def check_status(self):
        status_list = self.status
        if len(status_list) > 1:
            if status_list[-2] != status_list[-1]:
                return True
            else:
                return False
        else:
            return

    def add_status_flag_to_gs(self):
        #adding row of host name, ip, status and timestamp to Google Sheets
        parser = self.parser
        now = datetime.now()
        if self.check_status():
            parser.parse_next_free_row('A', self.host_name)
            parser.parse_next_free_row('B', self.ip)
            parser.parse_next_free_row('C', self.status[-1])
            parser.parse_next_free_row('D', str(now))
        else:
            return

