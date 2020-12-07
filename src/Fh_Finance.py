import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font
import re
import json
import time

"""
https://tech.ifeng.com/24h/
http://tech.ifeng.com/
http://finance.ifeng.com/
"""

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class FengHuang(object):
    def __init__(self, filename):
        self.xlsxname = filename

    def request(self):
        #new
        self.url = 'http://finance.ifeng.com/'
        self.data = requests.get(self.url, headers=headers)
        self.soup = BeautifulSoup(self.data.text, "lxml")

        self.stock_url = 'http://finance.ifeng.com/stock/'
        self.stock_data = requests.get(self.stock_url, headers=headers)
        self.stock_soup = BeautifulSoup(self.stock_data.text, "lxml")

    def getTopNew(self):
        wb = load_workbook(self.xlsxname)
        sheet = wb.create_sheet("Fh")
        t_row = 1
        t_col = 1
        sheet.cell(row=t_row, column=t_col, value="凤凰财经")
        t_row = t_row + 1
        sheet.cell(row=t_row, column=t_col, value="新闻标题")
        sheet.cell(row=t_row, column=t_col + 1, value="新闻链接")
        sheet.cell(row=t_row, column=t_col + 2, value="新闻简介")
        sheet.cell(row=t_row, column=t_col + 3, value="新闻时间")
        t_row = t_row + 1

        datalist = self.soup.find_all(class_='hot-1NJ2DKa4 clearfix')

        for New in datalist:
            for news in New:
                m_new = news.find('a')
                m_title = m_new['title']
                m_href = m_new['href']
                sheet.cell(row=t_row, column=t_col, value=m_title)
                sheet.cell(row=t_row, column=t_col + 1, value=m_href)
                t_row = t_row + 1

        try:
            wb.save(self.xlsxname)
        except:
            print("FengHuang Save Error = getTopNew")

    """
    def getNew2(self): #要闻
        wb = load_workbook(self.xlsxname)
        sheet = wb.get_sheet_by_name("Fh")
        t_row = sheet.max_row + 1
        t_col = 1
        sheet.cell(row=t_row, column=t_col, value="财经要闻")
        t_row = t_row + 1
        sheet.cell(row=t_row, column=t_col, value="新闻标题")
        sheet.cell(row=t_row, column=t_col + 1, value="新闻链接")
        sheet.cell(row=t_row, column=t_col + 2, value="新闻简介")
        sheet.cell(row=t_row, column=t_col + 2, value="新闻时间")
        t_row = t_row + 1

        #datalist = self.soup.find_all(class_='list-1D1mq9N- clearfix')
        datalist = self.soup.find_all(class_='text-2iuwVuE4')
        print(datalist)
    """

    def getStockNews(self):
        wb = load_workbook(self.xlsxname)
        sheet = wb.get_sheet_by_name("Fh")
        t_row = sheet.max_row + 2
        t_col = 1
        sheet.cell(row=t_row, column=t_col, value="证券要闻")
        t_row = t_row + 1
        sheet.cell(row=t_row, column=t_col, value="新闻标题")
        sheet.cell(row=t_row, column=t_col + 1, value="新闻链接")
        sheet.cell(row=t_row, column=t_col + 2, value="新闻简介")
        sheet.cell(row=t_row, column=t_col + 3, value="新闻时间")
        t_row = t_row + 1
        soup = str(self.stock_soup)

        #sear = re.search(r'var allData = (.*?) .*\"\}\}\;', soup, re.M | re.I)
        sear = re.search('var allData = (.*?)var adData', soup, re.M | re.I | re.S)
        data = sear.group(1)
        data = data.replace(";", "")
        json_str = json.loads(data)
        print(data)
        stockNews = json_str['stockNews']
        for m_new in stockNews:
            m_title = m_new['title']
            href = m_new['url']
            m_href = href.replace("//", "https://")

            sheet.cell(row=t_row, column=t_col, value=m_title)
            sheet.cell(row=t_row, column=t_col + 1, value=m_href)
            t_row = t_row + 1

        try:
            wb.save(self.xlsxname)
        except:
            print("FengHuang Save Error = getStockNews")


    def main(self, filename):
        Fh = FengHuang(filename)
        #Fh.Style()
        Fh.request()
        Fh.getTopNew()
        Fh.getStockNews()
"""
stockNews
stockNewsList
news
newsList
bannerPic
marketAnalysis
hotPlate
gnin
gnout
track
fiveDaysBuy
fiveDaysSell
logs
"""