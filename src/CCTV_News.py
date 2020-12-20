import requests
from bs4 import BeautifulSoup
import json
import threading
import time
import re
import os

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    #'Cookie': 'xqat=3e14cc861fdd960a5d84e7316165286b1bfeafe3;',
}

class CCTV_News(object):
    def __init__(self):
        # 央视新闻联播文字版
        # http://xwlbo.com/txt.html
        pass

    def request(self):
        url = 'http://xwlbo.com/txt.html'
        newslist = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(newslist.text, "lxml")


    def getNews_url(self):
        newslist = self.soup.select('#tab_con1 > div > ol > li:nth-child(1)')
        self.News_url = ""
        for news in newslist:
            self.News_url = news.find('a')['href']
            self.News_title = news.find('a').get_text().replace('文字完整版内容', '')


    filename = ""
    def getNews(self):
        news = requests.get(self.News_url, headers=headers)
        soup = BeautifulSoup(news.text, "lxml")
        content = soup.find_all(class_='text_content')
        self.filename = self.News_title + ".md"
        with open(self.filename, "w+") as f:
            for news in content:
                m_con = news.find_all('p')
                for m_cont in m_con:
                    m_content = m_cont.get_text()
                    f.write("- " + m_content + "\n")

    def getfilename(self):
        return self.filename

    def main(self):
        CCTV = CCTV_News()
        CCTV.request()
        CCTV.getNews_url()
        #t1 = threading.Thread(target=CCTV.getNews, args=())
        #t1.start()
        CCTV.getNews()
        filename = CCTV.getfilename()
        return filename


