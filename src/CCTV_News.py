import requests
from bs4 import BeautifulSoup
import os
import shutil
from src.Platform import pt
import time

"""
http://mrxwlb.com/category/mrxwlb-text/amp/
cn.govopendata.com
http://www.11417.cn/cctv.html
"""

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class CCTV_News(object):
    def __init__(self):
        pass

    def request(self):
        newslist = ''
        url = 'http://mrxwlb.com/category/mrxwlb-text/amp/'
        for _ in range(10):
            try:
                newslist = requests.get(url, headers=headers)
                break
            except:
                continue
        self.soup = BeautifulSoup(newslist.text, "lxml")
        m_new = self.soup.find(class_='loop-title')
        m_url = m_new.find('a')
        self.mr_url = m_url['href']
        self.mr_title = m_url.get_text()


    def getNews(self):
        news = ''
        # self.mr_url = 'http://mrxwlb.com/2022年1月6日新闻联播文字版/amp/'
        # self.mr_title = '2022年1月6日新闻联播文字版'
        for _ in range(10):
            try:
                news = requests.get(self.mr_url, headers=headers)
                break
            except:
                continue
        soup = BeautifulSoup(news.text, "lxml")
        content = soup.find_all(class_='cntn-wrp artl-cnt')
        # 补全
        self.filename = self.mr_title + ".md"
        with open(self.filename, "w+", encoding='utf-8') as f:
            for news in content:
                m_con = news.find_all('li')
                m_con2 = news.find_all('p')
                for m_cont in m_con:
                    m_content = m_cont.get_text()
                    f.write("- " + m_content + "\n")
                f.write("---" + "\n")
                for m_cont in m_con2:
                    m_content = m_cont.get_text()
                    f.write("- " + m_content + "\n")

        if pt.get_platform() == True:
            self.win_cctv_file(self.filename)
        else:
            self.lin_cctv_file(self.filename)


    def getfilename(self):
        return self.filename

    def lin_cctv_file(self, filename):
        path = "./Finance/CCTV_News/"
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

    def request_114(self):
        newslist = ''
        url = 'http://www.11417.cn/cctv.html'
        for _ in range(10):
            try:
                newslist = requests.get(url, headers=headers, timeout=30)
                break
            except:
                continue
        self.soup = BeautifulSoup(newslist.text, "lxml")
        m_new = self.soup.select('#hcsticky > div.content > div.block > div:nth-child(1) > h2 > a')
        self.m114_url = m_new[0]['href']
        self.m114_title = m_new[0].get_text()


    def getNews_114(self):
        news = ''
        # self.m_url = 'http://www.11417.cn/7309.html'
        # self.m_title = '2022年01月06日新闻联播文字版完整版'
        for _ in range(10):
            try:
                news = requests.get(self.m114_url, headers=headers, timeout=30)
                break
            except:
                continue

        soup = BeautifulSoup(news.text, "lxml")
        content = soup.find_all(class_='single')

        self.filename = self.m114_title + ".md"
        with open(self.filename, "w+", encoding='utf-8') as f:
            for news in content:
                #m_con = news.find_all('li')
                m_con2 = news.find_all('p')
                for m_cont in m_con2:
                    m_content = m_cont.get_text()
                    f.write("- " + m_content + "\n")

        if pt.get_platform() == True:
            self.win_cctv_file(self.filename)
        else:
            self.lin_cctv_file(self.filename)


    def main(self):
        #获取今天与昨天的新闻联播 已获取会自动覆盖
        CCTV.request()
        CCTV.getNews()
        CCTV.request_114()
        CCTV.getNews_114()


CCTV = CCTV_News()
