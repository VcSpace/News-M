import requests
from bs4 import BeautifulSoup
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
        #http://www.xwlb.net.cn/video.html
        pass

    def request(self):
        url = 'http://www.xwlb.net.cn/video.html'
        newslist = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(newslist.text, "lxml")
        m_new = self.soup.find(class_='post_body')
        new_url = m_new.find_all('a')
        self.new_url = " "
        self.new_name = " "
        for n in new_url:
            self.new_url = n['href']
            self.new_name = n['title']
            break

    def getNews(self):
        news = requests.get(self.new_url, headers=headers)
        soup = BeautifulSoup(news.text, "lxml")
        content = soup.find_all(class_='content')
        self.filename = self.new_name + ".md"
        with open(self.filename, "w+", encoding='utf-8') as f:
            for news in content:
                m_con = news.find_all('p')
                for m_cont in m_con:
                    m_content = m_cont.get_text()
                    f.write("- " + m_content + "\n")

        if pt.get_platform() == True:
            self.win_cctv_file(self.filename)
        else:
            self.lin_cctv_file(self.filename)


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

    def main(self):
        #获取今天与昨天的新闻联播 已获取会自动覆盖
        CCTV.request()
        CCTV.getNews()


CCTV = CCTV_News()
