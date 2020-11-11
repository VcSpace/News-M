import requests
from bs4 import BeautifulSoup
import xlrd, xlwt
import xlutils
import json
from requests.cookies import RequestsCookieJar

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    #'Cookie': 'xqat=3e14cc861fdd960a5d84e7316165286b1bfeafe3;',
}

class SelfStock(object):
    def __init__(self, file_name):
        self.xlsxname = file_name

    def Style(self):
        font = xlwt.Font()  # 内容字体
        font2 = xlwt.Font()  # 标题字体
        font3 = xlwt.Font()  # 指数
        font.height = 20 * 11
        font2.height = 20 * 12
        font2.bold = True
        font3.height = 20 * 13
        self.style = xlwt.XFStyle() #标题 链接字体
        self.style_head = xlwt.XFStyle() #类别列字体
        self.style_index = xlwt.XFStyle() #指数字体

        self.style.font = font
        self.style_head.font = font2
        self.style_index.font = font3

    def Deal_Xq_data(self):
        print(1)


    def get_SelfStock(self):
        url_list = list()
        with open("Code.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                sep = '#'
                line = line.split(sep, 1)[0]
                if line != '':
                    #url = 'https://xueqiu.com/S/{}'.format(line)
                    url = 'https://stock.xueqiu.com/v5/stock/batch/quote.json?extend=detail&is_delay_ft=1&is_delay_hk=0&symbol={}'.format(line)
                    url_list.append(url)

        url = 'https://xueqiu.com'
        session = requests.session()
        session.get(url, headers=headers)
        for url in url_list:
            resp = session.get(url, headers=headers)
            data = json.loads(resp.text)
            self.Deal_Xq_data()
            print(data)
            #data = requests.get(url, headers=headers)


    def main(self, file_name):
        Stock = SelfStock(file_name)
        Stock.Style()
        Stock.get_SelfStock()
