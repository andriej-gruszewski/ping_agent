import gspread as gs
import time
import random


class GSP_Parser:

    def __init__(self, token, url, sheet_name):
        self.token = token
        self.url = url
        self.sheet_name = sheet_name

    def connect_to_sheet(self):
        # estabilishment of connection to Goggle Sheet as your database file
        gc = gs.service_account_from_dict(self.token)
        sh = gc.open_by_url(self.url)
        ws = sh.worksheet(self.sheet_name)
        return ws

    def next_available_row(self, ws, column_number):
        # recognizing next free row in your Google Sheet, where new status can be written
        random_int = random.randint(1, 6)
        time.sleep(random_int)
        str_list = list(ws.col_values(column_number))
        return len(str_list) + 1

    def parse_next_free_row(self, column, value):
        # parsin status to next free row in Google Sheet database
        num = 31
        lower_column = str.lower(column)
        ws = self.connect_to_sheet()
        return ws.update_acell(f'{column}{self.next_available_row(ws, (ord(lower_column)) & num)}', value)
