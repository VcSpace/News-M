import requests
from bs4 import BeautifulSoup
import os
import shutil
from src.Platform import pt
import time

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
        m_new = self.soup.select('body > div.content-wrapper > div.cntr.archive > div.arch-dsgn > div > div.loop-wrapper > div:nth-child(1) > div > h3 > a')
        self.m_url = m_new[0]['href']
        self.m_title = m_new[0].get_text()

        # alist = list()
        # cnum = 13
        # while cnum < 26:
        #     m = '2021年11月{0}日新闻联播文字版'.format(cnum)
        #     cnum = cnum + 1
        #     alist.append(m)
        #
        # for ml in alist:
        #     self.m_title = ml
        #     self.m_url = 'http://mrxwlb.com/{0}/amp/'.format(ml)
        #     self.getNews()
        #     time.sleep(10)

    def getNews(self):
        news = ''
        for _ in range(10):
            try:
                news = requests.get(self.m_url, headers=headers)
                break
            except:
                continue
        soup = BeautifulSoup(news.text, "lxml")
        content = soup.find_all(class_='cntn-wrp artl-cnt')
        # 补全
        self.filename = self.m_title + ".md"
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

    def main(self):
        #获取今天与昨天的新闻联播 已获取会自动覆盖
        CCTV.request()
        CCTV.getNews()


CCTV = CCTV_News()
