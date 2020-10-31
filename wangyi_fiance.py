import requests
from bs4 import BeautifulSoup
import os
import xlrd
import xlwt
from xlutils.copy import copy
import json
import time

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class WangYi(object):
    def __init__(self):
        #new
        self.url = 'https://money.163.com/'
        self.data = requests.get(self.url, headers=headers)
        self.xlsxname = "C:\\Users\\Vcvc\\Desktop\\WangyiFinance.xlsx"

        #stock
        self.stockurl = 'https://money.163.com/stock/'
        self.stockdata = requests.get(self.stockurl, headers=headers)

        #index
        self.time = time.time()
        self.indexurl = 'http://api.money.126.net/data/feed/1399001,1399300,0000001,HSRANK_COUNT_SHA,HSRANK_COUNT_SZA,HSRANK_COUNT_SH3?callback=ne_{}&[object%20Object]'.format(int(self.time))
        self.indexdata = requests.get(self.indexurl, headers=headers)

    def getTopNew(self):
        print("要闻 ")
        soup = BeautifulSoup(self.data.text, "lxml")
        datalist = soup.select("ul li h2")
        #datalist = soup.find_all(class_="topnews_nlist topnews_nlist1")

        wbook = xlwt.Workbook()
        wsheet = wbook.add_sheet('wy', cell_overwrite_ok=True)
        style = xlwt.easyxf('align: vertical center, horizontal center')
        """
        alignment = xlwt.Alignment
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
        style2 = xlwt.XFStyle()
        style2.alignment = alignment
        """

        wsheet.write(4, 0, u'新闻标题', style)
        wsheet.write(4, 1, u'新闻链接', style)
        wsheet.write(4, 2, u'新闻时间', style)
        wsheet.write(4, 3, u'内容简介', style)

        t_row = 5
        t_col = 0
        for li in datalist:
            url = li.find('a')['href']
            title = li.get_text()
            wsheet.write(t_row, t_col, title)
            wsheet.write(t_row, t_col + 1, url)
            t_row = t_row + 1
        try:
            wbook.save(self.xlsxname)
        except:
            print('Save error')
        else:
            print('excel save')

    def getlist2(self):
        soup = BeautifulSoup(self.data.text, "lxml")
        datalist2 = soup.find_all(class_='topnews_nlist topnews_nlist2')

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(0)

        table = xlsxin.sheets()[0]
        ow = table.nrows

        t_row = ow
        t_col = 0
        for tp in datalist2:
            datalist3 = tp.select("li h3")
            for tn in datalist3:
                url = tn.find('a')['href']
                title = tn.get_text()
                wb.write(t_row, t_col, title)
                wb.write(t_row, t_col + 1, url)
                t_row = t_row + 1
        try:
            sheet.save(self.xlsxname)
        except:
            print("Save Error")
        else:
            print("Save Success")

    def getstock(self):
        soup = BeautifulSoup(self.stockdata.text, 'lxml')
        stockl = soup.select('#stock2016_wrap > div > div.stock2016_content > div.idx_main.common_wrap.clearfix > div.news_main > div.news_main_wrap > div.topnews > div.topnews_first > h2 > a')
        top_url = stockl[0]['href']
        top_title = stockl[0].get_text()

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[0]
        ow = table.nrows #已经使用多少行
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(0)

        t_row = ow
        t_col = 0
        wb.write(t_row, t_col, top_title)
        wb.write(t_row, t_col + 1, top_url)
        t_row = t_row + 1

        stocknewlist = soup.find_all(class_='topnews_list')
        for s_new in stocknewlist:
            news = s_new.find_all('a')
            for tn in news:
                t_url = tn['href']
                t_title = tn.get_text()
                wb.write(t_row, t_col, t_title)
                wb.write(t_row, t_col + 1, t_url)
                t_row = t_row + 1
        try:
            sheet.save(self.xlsxname)
        except:
            print("Save Error")
        else:
            print("Save Success")

    def get_num(self, num, row):
        num_price = num['price']
        num_open = num['open']
        num_updown = num['updown']
        num_high = num['high']
        num_low = num['low']
        num_yestclose = num['yestclose']
        num_percent = num['percent'] #num_percent 不直接写入
        num_update = num['update']
        m_percent = num_percent * 10000 #-0.020937 -%2.09
        percent = int(m_percent) /100

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[0]
        #ow = table.nrows  # 已经使用多少行
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(0)

        wb.write(0, 0, u'大盘指数')
        wb.write(0, 1, u'当前价位')
        wb.write(0, 2, u'今日涨幅')
        wb.write(0, 3, u'涨跌价格')
        wb.write(0, 4, u'开盘价位')
        wb.write(0, 5, u'今日最高')
        wb.write(0, 6, u'今日最低')
        wb.write(0, 7, u'昨日收盘')
        wb.write(0, 8, u'更新时间')
        wb.write(1, 0, u'上证指数')
        wb.write(2, 0, u'深证成指')
        wb.write(3, 0, u'沪深300')

        wb.write(row, 1, num_price)
        wb.write(row, 2, m_percent/100)
        wb.write(row, 3, num_updown)
        wb.write(row, 4, num_open)
        wb.write(row, 5, num_high)
        wb.write(row, 6, num_low)
        wb.write(row, 7, num_yestclose)
        wb.write(row, 8, num_update)

        try:
            sheet.save(self.xlsxname)
        except:
            print("Save Error")
        else:
            print("Save Success")
        wb.write(row, 8, num_update)


    def getindex(self):
        #soup = BeautifulSoup(self.indexdata.text,)
        data = self.indexdata.text + "del"
        time = int(self.time)
        data = data.replace('ne_' + str(time) + '(', '')
        data = data.replace(');del', '')
        #json_d = json.dumps(data)  # 编码
        json_str = json.loads(data)  # 解码

        n1 = json_str['0000001'] #上证指数_0000001
        n2 = json_str['1399001'] #深证成指_1399001
        n3 = json_str['1399300'] #沪深300_1399300
        self.get_num(n1, 1)
        self.get_num(n2, 2)
        self.get_num(n3, 3)



if __name__ == '__main__':
    Wy = WangYi()
    try:
        Wy.getTopNew()
        Wy.getlist2()
        #stock
        Wy.getstock()
        Wy.getindex()  # 主页原创栏目右边
    except Exception:
        print("获取TopNew失败")
