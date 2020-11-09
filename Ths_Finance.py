import requests
from bs4 import BeautifulSoup
import xlrd
import xlwt
from xlutils.copy import copy
import json
import time

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class TongHuaShun(object):
    def __init__(self, file_name):
        self.url = 'http://www.10jqka.com.cn/'
        self.data = requests.get(self.url, headers=headers)
        self.data.encoding = "gbk"
        self.soup = BeautifulSoup(self.data.text, "lxml")

        #calendar
        calendar_time = time.strftime("%Y%m", time.localtime())  # year-month-day-hour-minute
        #self.url_calendar = 'http://stock.10jqka.com.cn/fincalendar.shtml#{}'.format(datatime)
        self.url_calendar = 'http://comment.10jqka.com.cn/tzrl/getTzrlData.php?callback=callback_dt&type=data&date={}'.format(calendar_time)
        self.data_calendar = requests.get(self.url_calendar, headers=headers)

        #self.xlsxname = "C:\\Users\\Vcvc\\Desktop\\News_Finance.xlsx"
        self.xlsxname = file_name

    def Style(self):
        font = xlwt.Font() #内容字体
        font2 = xlwt.Font() #标题字体
        font.height = 20 * 11
        font2.height = 20 * 12
        font2.bold = True
        self.style = xlwt.XFStyle()
        self.style.font = font
        self.style_head = xlwt.XFStyle()
        self.style_head.font = font2


    def getNew(self):
        datalist = self.soup.find_all(class_="item_txt")
        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        sheet = copy(xlsxin)
        sheet.add_sheet('ths')
        wb = sheet.get_sheet(1)

        wb.write(0, 0, "同花顺财经", self.style_head)
        wb.write(1, 0, "新闻标题", self.style_head)
        wb.write(1, 1, "新闻链接", self.style_head)
        wb.write(1, 2, "新闻简介", self.style_head)
        wb.write(1, 3, "新闻时间", self.style_head)

        t_row = 2
        t_col = 0
        for news in datalist:
            newlist2 = news.select('p a')
            for m_new in newlist2:
                m_url = m_new['href']
                m_title = m_new['title']
                wb.write(t_row, t_col, m_title, self.style)
                wb.write(t_row, t_col + 1, m_url, self.style)
                t_row = t_row + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("THS Save Error = 1")

    def getInvestment(self):
        datalist = self.soup.find_all(class_="content newhe") #投资机会上半部分 产经新闻 研报精选

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[1]
        t_row = table.nrows  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(1)

        index = 0
        for newlist in datalist:
            #里面有个重复 加个判断去掉
            news = newlist.select('li a')
            for m_new in news:
                if index != 1:
                    m_url = m_new['href']
                    m_title = m_new['title']
                    wb.write(t_row, t_col, m_title, self.style)
                    wb.write(t_row, t_col + 1, m_url, self.style)
                    t_row = t_row + 1
                index = index + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("THS Save Error = 2")

    def getInvestment2(self):
        #投资机会后半部分获取
        datalist = self.soup.find_all(class_="last")

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[1]
        t_row = table.nrows  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(1)

        i = 0
        for newlist in datalist:
            news = newlist.select('li a')
            for m_new in news:
                #这个分类筛选的结果重复的太多  但是数量是固定的
                if i >= 5:
                    if i < 11:
                        m_title = m_new.get_text()
                        m_url = m_new['href']
                        wb.write(t_row, t_col, m_title, self.style)
                        wb.write(t_row, t_col + 1, m_url, self.style)
                        t_row = t_row + 1
                i = i + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("THS Save Error = 3")

    def get_Newspaper(self):
        url_Newspaper = 'http://stock.10jqka.com.cn/bktt_list/'
        data_paper = requests.get(url_Newspaper, headers=headers)
        soup_paper = BeautifulSoup(data_paper.text, "lxml")

        datalist = soup_paper.select('body > div.content-1200 > div.module-l.fl > div.list-con > ul > li:nth-child(1) > span > a')
        datalist2 = soup_paper.select('body > div.content-1200 > div.module-l.fl > div.list-con > ul > li:nth-child(1) > a')
        m_url = datalist[0]['href']
        m_title = datalist[0]['title']
        m_content = datalist2[0].get_text() + "del"
        m_content = m_content.replace("...del", "")

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[1]
        t_row = table.nrows  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(1)
        wb.write(t_row + 1, t_col, "报刊头条", self.style_head) #下一个函数省一次xlwt操作 (投资日历)
        t_row = t_row + 2
        wb.write(t_row, t_col, m_title, self.style)
        wb.write(t_row, t_col + 1, m_url, self.style)
        wb.write(t_row, t_col + 2, m_content, self.style)

        # 为下一个函数省一次xlwt操作 (投资日历)
        wb.write(t_row + 2, t_col, "投资日历", self.style_head)
        wb.write(t_row + 3 , t_col, "会议事件", self.style_head)
        wb.write(t_row + 3, t_col + 1, "会议地点", self.style_head)
        wb.write(t_row + 3, t_col + 2, "会议时间", self.style_head)

        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("THS Save Error = 4")

    def dealjson(self, json): #时间 事件 地点 json问题相关板块顺序是乱序 就不加了
        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[1]
        t_row = table.nrows # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(1)

        for json_event in json['events']:
            m_event = json_event[0]
            m_place = json_event[2]
            wb.write(t_row, t_col, m_event, self.style)
            wb.write(t_row, t_col + 1, m_place, self.style)
            m_date = json['date']
            m_week = json['week']
            wb.write(t_row, t_col + 2, m_date + "-" + m_week, self.style)
            t_row = t_row + 1

        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("THS Save Error = 5")


    def get_Calendar(self): #投资日历
        data = self.data_calendar.text + "del"
        data = data.replace("callback_dt(", "")
        data = data.replace(");del", "")
        json_str = json.loads(data)
        #m_json = json_str['data'][0]
        t = 0
        for m_json in json_str['data']:
            self.dealjson(m_json)


    def main(self, file_name):
        Ths = TongHuaShun(file_name)
        Ths.Style()
        Ths.getNew()
        Ths.getInvestment()
        Ths.getInvestment2()
        Ths.get_Newspaper()
        Ths.get_Calendar()
