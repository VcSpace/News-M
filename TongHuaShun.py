import requests
from bs4 import BeautifulSoup
import os
import xlrd
import xlwt
from xlutils.copy import copy
import json
import chardet

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class TongHua():
    def __init__(self):
        self.url = 'http://www.10jqka.com.cn/'
        self.data = requests.get(self.url, headers=headers)
        self.data.encoding = "gbk"

    def getNew(self):
        soup = BeautifulSoup(self.data.text, "lxml")
        datalist = soup.find_all(class_="item_txt")

        for news in datalist:
            newlist2 = news.select('p a')
            for m_new in newlist2:
                m_url = m_new['href']
                m_title = m_new['title']
        #缺少写入


    def main(self):
        Ths = TongHua()
        Ths.getNew()
        """
        try:
        except Exception:
            print("TongHua Get Error")
        """
