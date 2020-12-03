import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl.styles import Font
import json
import time

"""
https://tech.ifeng.com/24h/
http://tech.ifeng.com/
http://finance.ifeng.com/
"""

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class FengHuang(object):
    def __init__(self, filename):
        self.xlsxname = filename

    def getTopNew(self):


    def main(self, filename):
        Fh = FengHuang(filename)
        #Fh.Style()
        Fh.getTopNew()
