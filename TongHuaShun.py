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

class TongHua(object):
    def __init__(self, file_name):
        self.url = 'http://www.10jqka.com.cn/'
        self.data = requests.get(self.url, headers=headers)
        self.data.encoding = "gbk"
        self.soup = BeautifulSoup(self.data.text, "lxml")

        #self.xlsxname = "C:\\Users\\Vcvc\\Desktop\\News_Finance.xlsx"
        self.xlsxname = file_name

    def getNew(self):
        datalist = self.soup.find_all(class_="item_txt")
        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        sheet = copy(xlsxin)
        sheet.add_sheet('ths')
        wb = sheet.get_sheet(1)

        wb.write(0, 0, "同花顺财经")
        wb.write(1, 0, "新闻标题")
        wb.write(1, 1, "新闻链接")
        wb.write(1, 2, "新闻时间")
        wb.write(1, 3, "内容简介")

        t_row = 2
        t_col = 0
        for news in datalist:
            newlist2 = news.select('p a')
            for m_new in newlist2:
                m_url = m_new['href']
                m_title = m_new['title']
                wb.write(t_row, t_col, m_title)
                wb.write(t_row, t_col + 1, m_url)
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
                    wb.write(t_row, t_col, m_title)
                    wb.write(t_row, t_col + 1, m_url)
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
                        wb.write(t_row, t_col, m_title)
                        wb.write(t_row, t_col + 1, m_url)
                        t_row = t_row + 1
                i = i + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("THS Save Error = 3")


    def main(self, file_name):
        Ths = TongHua(file_name)
        Ths.getNew()
        Ths.getInvestment()
        Ths.getInvestment2()
