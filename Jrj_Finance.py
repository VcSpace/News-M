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
        url = 'http://finance.jrj.com.cn/'
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, "lxml")

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        sheet = copy(xlsxin)
        sheet.add_sheet('jrj')
        wb = sheet.get_sheet(2)

        wb.write(0, 0, "金融界财经", self.style_head)
        wb.write(1, 0, "新闻标题", self.style_head)
        wb.write(1, 1, "新闻链接", self.style_head)
        wb.write(1, 2, "新闻简介", self.style_head)
        wb.write(1, 3, "新闻时间", self.style_head)
        t_row = 2
        t_col = 0

        datalist = soup.find_all(class_="l1_top")
        for News in datalist:
            New = News.select('dl dt p')
            for m_new in New:
                data = m_new.find('a')
                m_url = data['href']
                m_title = data.get_text()
                wb.write(t_row, t_col, m_title, self.style)
                wb.write(t_row, t_col + 1, m_url, self.style)
                t_row = t_row + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("JRJ Save Error = 1")

    def get_FinanceNews(self): #差不多4-5个小时内的热点新闻
        fin_time1 = time.strftime("%Y%m", time.localtime())  # year-month-day-hour-minute
        fin_time2 = time.strftime("%Y%m%d", time.localtime())  # year-month-day-hour-minute
        fin_url = 'http://finance.jrj.com.cn/xwk/{}/{}_1.shtml'.format(fin_time1, fin_time2)

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[2]
        t_row = table.nrows  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(2)

        wb.write(t_row + 1, t_col, "财经频道新闻", self.style_head)
        wb.write(t_row + 2, t_col, "新闻标题", self.style_head)
        wb.write(t_row + 2, t_col + 1, "新闻链接", self.style_head)
        wb.write(t_row + 2, t_col + 2, "新闻简介", self.style_head)
        wb.write(t_row + 2, t_col + 3, "新闻时间", self.style_head)
        t_row = t_row + 3
        time_row = t_row

        data = requests.get(fin_url, headers=headers)
        soup = BeautifulSoup(data.text, "lxml")
        datalist = soup.find_all(class_="list")
        flag = False
        for Newslist in datalist:
            #News = Newslist.select('li')
            News = Newslist.find_all('a')
            m_NewsTime = Newslist.find_all('span')
            for m_new in News:
                if flag == True:
                    flag = False
                    m_url = m_new['href']
                    m_title = m_new.get_text()
                    wb.write(t_row, t_col, m_title, self.style)
                    wb.write(t_row, t_col + 1, m_url, self.style)
                    t_row = t_row + 1
                else:
                    flag = True
            for new_time in m_NewsTime:
                m_time = new_time.get_text()
                wb.write(time_row, t_col + 3, m_time, self.style)
                time_row = time_row + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("JRJ Save Error = 2")

    def get_todayHot(self):
        url = 'http://biz.jrj.com.cn/biz_index.shtml'
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, "lxml")
        datalist = soup.find_all(class_="jrj-top10")

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[2]
        t_row = table.nrows + 1  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(2)

        wb.write(t_row, t_col, "24小时间热闻点击排行榜", self.style_head)
        t_row = t_row + 1
        wb.write(t_row, t_col, "新闻标题", self.style_head)
        wb.write(t_row, t_col + 0, "新闻标题", self.style_head)
        wb.write(t_row, t_col + 1, "新闻链接", self.style_head)
        wb.write(t_row, t_col + 2, "新闻简介", self.style_head)
        wb.write(t_row, t_col + 3, "新闻时间", self.style_head)
        t_row = t_row + 1

        flag = True
        for Newslist in datalist:
            if flag == True:
                News = Newslist.find_all('a')
                for m_new in News:
                    m_title = m_new['title']
                    m_url = m_new['href']
                    wb.write(t_row, t_col, m_title, self.style)
                    wb.write(t_row, t_col + 1, m_url, self.style)
                    t_row = t_row + 1
            flag = False
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("JRJ Save Error = 5")


    def get_Business(self):
        bu_time1 = time.strftime("%Y%m", time.localtime())  # year-month-day-hour-minute
        bu_time2 = time.strftime("%Y%m%d", time.localtime())  # year-month-day-hour-minute
        bus_url = 'http://biz.jrj.com.cn/xwk/{}/{}_1.shtml'.format(bu_time1, bu_time2)

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[2]
        t_row = table.nrows  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(2)

        wb.write(t_row + 1, t_col, "商业频道新闻", self.style_head)
        wb.write(t_row + 2, t_col, "新闻标题", self.style_head)
        wb.write(t_row + 2, t_col + 1, "新闻链接", self.style_head)
        wb.write(t_row + 2, t_col + 2, "新闻简介", self.style_head)
        wb.write(t_row + 2, t_col + 3, "新闻时间", self.style_head)
        t_row = t_row + 3
        time_row = t_row

        data = requests.get(bus_url, headers=headers)
        soup = BeautifulSoup(data.text, "lxml")
        datalist = soup.find_all(class_="list")
        flag = False
        for Newslist in datalist:
            # News = Newslist.select('li')
            News = Newslist.find_all('a')
            m_NewsTime = Newslist.find_all('span')
            for m_new in News:
                if flag == True:
                    flag = False
                    m_url = m_new['href']
                    m_title = m_new.get_text()
                    wb.write(t_row, t_col, m_title, self.style)
                    wb.write(t_row, t_col + 1, m_url, self.style)
                    t_row = t_row + 1
                else:
                    flag = True
            for new_time in m_NewsTime:
                m_time = new_time.get_text()
                wb.write(time_row, t_col + 3, m_time, self.style)
                time_row = time_row + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("JRJ Save Error = 3")

    def get_Science(self):
        sci_time1 = time.strftime("%Y%m", time.localtime())  # year-month-day-hour-minute
        sci_time2 = time.strftime("%Y%m%d", time.localtime())  # year-month-day-hour-minute
        sci_url = 'http://biz.jrj.com.cn/xwk/{}/{}_1.shtml'.format(sci_time1, sci_time2)

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[2]
        t_row = table.nrows  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(2)

        wb.write(t_row + 1, t_col, "科技频道新闻", self.style_head)
        wb.write(t_row + 2, t_col, "新闻标题", self.style_head)
        wb.write(t_row + 2, t_col + 1, "新闻链接", self.style_head)
        wb.write(t_row + 2, t_col + 2, "新闻简介", self.style_head)
        wb.write(t_row + 2, t_col + 3, "新闻时间", self.style_head)
        t_row = t_row + 3
        time_row = t_row

        data = requests.get(sci_url, headers=headers)
        soup = BeautifulSoup(data.text, "lxml")
        datalist = soup.find_all(class_="list")
        flag = False
        for Newslist in datalist:
            # News = Newslist.select('li')
            News = Newslist.find_all('a')
            m_NewsTime = Newslist.find_all('span')
            for m_new in News:
                if flag == True:
                    flag = False
                    m_url = m_new['href']
                    m_title = m_new.get_text()
                    wb.write(t_row, t_col, m_title, self.style)
                    wb.write(t_row, t_col + 1, m_url, self.style)
                    t_row = t_row + 1
                else:
                    flag = True
            for new_time in m_NewsTime:
                m_time = new_time.get_text()
                wb.write(time_row, t_col + 3, m_time, self.style)
                time_row = time_row + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("JRJ Save Error = 4")

    def main(self, filename):
        Jrj = JinRongJie(filename)
        Jrj.Style()
        Jrj.get_TopNews()
        Jrj.get_todayHot()
        Jrj.get_FinanceNews()
        Jrj.get_Business()
        Jrj.get_Science()

