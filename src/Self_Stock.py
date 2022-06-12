import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook, Workbook
import json
import threading
import time
import re
import os
import wget
from src.Platform import pt

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class SelfStock(object):
    threadLock = threading.Lock()
    def __init__(self):
        self.stop = True
        #self.xlsxname = file_name


Stock = SelfStock()
