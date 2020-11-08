import requests
from bs4 import BeautifulSoup
import xlrd, xlwt
from xlutils.copy import copy
import json
import time

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class JinRongJie(object):
    def __init__(self, filename):
        self.xlsxname = filename
        self.url = 'http://finance.jrj.com.cn/'
        self.data = requests.get(self.url, headers=headers)
        self.soup = BeautifulSoup(self.data.text, "lxml")


    def Style(self):
        font = xlwt.Font()  # 内容字体
        font2 = xlwt.Font()  # 标题字体
        font3 = xlwt.Font()  # 指数
        font.height = 20 * 11
        font2.height = 20 * 12
        font2.bold = True
        font3.height = 20 * 13
        self.style = xlwt.XFStyle()  # 标题 链接字体
        self.style_head = xlwt.XFStyle()  # 类别列字体
        self.style_index = xlwt.XFStyle()  # 指数字体

        self.style.font = font
        self.style_head.font = font2
        self.style_index.font = font3


    def get_TopNews(self):
        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        sheet = copy(xlsxin)
        sheet.add_sheet('jrj')
        wb = sheet.get_sheet(2)

        wb.write(0, 0, "金融界财经", self.style_head)
        wb.write(1, 0, "新闻标题", self.style_head)
        wb.write(1, 1, "新闻链接", self.style_head)
        wb.write(1, 2, "新闻链接", self.style_head)
        wb.write(1, 3, "新闻时间", self.style_head)
        t_row = 2
        t_col = 0

        datalist = self.soup.find_all(class_="l1_top")
        for News in datalist:
            New = News.select('dl dt p')
            for m_new in New:
                data = m_new.find('a')
                m_url = data['href']
                m_title = data.get_text()
                wb.write(t_row, t_col, m_title)
                wb.write(t_row, t_col + 1, m_url)
                t_row = t_row + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("JRJ Save Error = 1")


    def main(self, filename):
        Jrj = JinRongJie(filename)
        Jrj.Style()
        Jrj.get_TopNews()

