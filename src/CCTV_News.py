import requests
from bs4 import BeautifulSoup
import json
import threading
import time
import re
import os
import shutil
from src.Platform import pt

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
        newslist2 = self.soup.select('#tab_con1 > div > ol > li:nth-child(2)')
        os = self.get_os()
        for news in newslist:
            News_url = news.find('a')['href']
            News_title = news.find('a').get_text().replace('文字完整版内容', '')
            self.getNews(os, News_url, News_title)

        for news2 in newslist2:
            News_url2 = news2.find('a')['href']
            News_title2 = news2.find('a').get_text().replace('文字完整版内容', '')
            self.getNews(os, News_url2, News_title2)


    filename = ""
    def getNews(self, os, url, title):
        news = requests.get(url, headers=headers)
        soup = BeautifulSoup(news.text, "lxml")
        content = soup.find_all(class_='text_content')
        self.filename = title + ".md"
        with open(self.filename, "w+") as f:
            for news in content:
                m_con = news.find_all('p')
                for m_cont in m_con:
                    m_content = m_cont.get_text()
                    f.write("- " + m_content + "\n")

        if os == True:
            self.win_cctv_file(self.filename)
        elif os == False:
            self.lin_cctv_file(self.filename)

    def getfilename(self):
        return self.filename

    def get_os(self):
        flag = pt.get_platform()
        return flag

    def lin_cctv_file(self, filename):
        path = "./Finance/CCTV_News/"
        filename = "./" + filename
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
        shutil.move(filename, path + filename)

    def win_cctv_file(self, cctv_file):
        desktop_path = os.path.join(os.path.expanduser('~'),"Desktop") #获取桌面路径
        path = desktop_path +"\\Finance\\CCTV_News\\"
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)

        shutil.move(cctv_file, path + cctv_file)

    def main(self):
        CCTV = CCTV_News()
        CCTV.request()
        CCTV.getNews_url()


