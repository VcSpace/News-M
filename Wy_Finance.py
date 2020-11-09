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
    def __init__(self, file_name):
        #new
        self.url = 'https://money.163.com/'
        self.data = requests.get(self.url, headers=headers)
        self.soup = BeautifulSoup(self.data.text, "lxml")
        #self.xlsxname = "C:\\Users\\Vcvc\\Desktop\\News_Finance.xlsx"

        self.xlsxname = file_name
        self.time = time.time()

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


    def getTopNew(self):
        datalist = self.soup.select("ul li h2")
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

        t_row = 5
        wsheet.write(t_row, 0, u"网易财经", self.style_head)
        t_row = t_row + 1
        t_col = 0
        wsheet.write(t_row, t_col, u'新闻标题', self.style_head)
        wsheet.write(t_row, t_col + 1, u'新闻链接', self.style_head)
        wsheet.write(t_row, t_col + 2, u'新闻简介', self.style_head)
        wsheet.write(t_row, t_col + 3, u'新闻时间', self.style_head)
        t_row = t_row + 1

        for li in datalist:
            url = li.find('a')['href']
            title = li.get_text()
            wsheet.write(t_row, t_col, title, self.style)
            wsheet.write(t_row, t_col + 1, url, self.style)
            t_row = t_row + 1
        try:
            wbook.save(self.xlsxname)
        except:
            print('Wangyi Save Error = 1')

    def getlist2(self):
        datalist2 = self.soup.find_all(class_='topnews_nlist topnews_nlist2')

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
                wb.write(t_row, t_col, title, self.style)
                wb.write(t_row, t_col + 1, url, self.style)
                t_row = t_row + 1
        try:
            sheet.save(self.xlsxname)
        except:
            print("Wangyi Save Error = 2")

    def getstock(self):
        #stock
        stockurl = 'https://money.163.com/stock/'
        stockdata = requests.get(stockurl, headers=headers)
        soup = BeautifulSoup(stockdata.text, "lxml")
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
        wb.write(t_row, t_col, top_title, self.style)
        wb.write(t_row, t_col + 1, top_url, self.style)
        t_row = t_row + 1

        stocknewlist = soup.find_all(class_='topnews_list')
        for s_new in stocknewlist:
            news = s_new.find_all('a')
            for tn in news:
                t_url = tn['href']
                t_title = tn.get_text()
                wb.write(t_row, t_col, t_title, self.style)
                wb.write(t_row, t_col + 1, t_url, self.style)
                t_row = t_row + 1
        try:
            sheet.save(self.xlsxname)
        except:
            print("Wangyi Save Error = 4")

    def get_num(self, num, row, if_write):
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

        if if_write == True:
            t_row = 0
            t_col = 0
            wb.write(t_row, t_col, u'大盘指数', self.style_head)
            wb.write(t_row, t_col + 1, u'当前价位', self.style_head)
            wb.write(t_row, t_col + 2, u'今日涨幅', self.style_head)
            wb.write(t_row, t_col + 3, u'涨跌价格', self.style_head)
            wb.write(t_row, t_col + 4, u'开盘价位', self.style_head)
            wb.write(t_row, t_col + 5, u'今日最高', self.style_head)
            wb.write(t_row, t_col + 6, u'今日最低', self.style_head)
            wb.write(t_row, t_col + 7, u'昨日收盘', self.style_head)
            wb.write(t_row, t_col + 8, u'更新时间', self.style_head)
            wb.write(t_row + 1, t_col, u'上证指数', self.style)
            wb.write(t_row + 2, t_col, u'深证成指', self.style)
            wb.write(t_row + 3, t_col, u'沪深300', self.style)

        wb.write(row, 1, num_price, self.style_index)
        wb.write(row, 2, str(percent) + "%", self.style_index)
        wb.write(row, 3, num_updown, self.style_index)
        wb.write(row, 4, num_open, self.style_index)
        wb.write(row, 5, num_high, self.style_index)
        wb.write(row, 6, num_low, self.style_index)
        wb.write(row, 7, num_yestclose, self.style_index)
        wb.write(row, 8, num_update, self.style_index)
        try:
            sheet.save(self.xlsxname)
        except:
            print("Wangyi Save Error = 5")


    def getindex(self):
        #index
        indexurl = 'http://api.money.126.net/data/feed/1399001,1399300,0000001,HSRANK_COUNT_SHA,HSRANK_COUNT_SZA,HSRANK_COUNT_SH3?callback=ne_{}&[object%20Object]'.format(int(self.time))
        indexdata = requests.get(indexurl, headers=headers)
        #soup = BeautifulSoup(self.indexdata.text,)
        data = indexdata.text + "del"
        time = int(self.time)
        data = data.replace('ne_' + str(time) + '(', '')
        data = data.replace(');del', '')
        #json_d = json.dumps(data)  # 编码
        json_str = json.loads(data)  # 解码

        if_write = True
        n1 = json_str['0000001'] #上证指数_0000001
        n2 = json_str['1399001'] #深证成指_1399001
        n3 = json_str['1399300'] #沪深300_1399300
        self.get_num(n1, 1, if_write)
        if_write = False
        self.get_num(n2, 2, if_write)
        self.get_num(n3, 3, if_write)

    def get_bu(self, soup, if_write):
        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[0]
        t_row = table.nrows  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(0)
        if if_write == True:
            wb.write(t_row + 1, t_col, "市场资讯", self.style_head)
            wb.write(t_row + 2, t_col, "新闻标题", self.style_head)
            wb.write(t_row + 2, t_col + 1, "新闻链接", self.style_head)
            wb.write(t_row + 2, t_col + 2, "新闻简介", self.style_head)
            wb.write(t_row + 2, t_col + 3, "新闻时间", self.style_head)
            t_row = t_row + 3  # 已经使用多少行

        datalist1 = soup.find_all(class_='list_item clearfix')
        for Newslist in datalist1:
            News = Newslist.find_all(class_='item_top')
            for m_new in News:
                m_new1 = m_new.find('a')
                m_new2 = m_new.find(class_='time')
                m_title = m_new1.get_text()
                m_url = m_new1['href']
                m_time = m_new2.get_text()
                wb.write(t_row, t_col, m_title, self.style)
                wb.write(t_row, t_col + 1, m_url, self.style)
                wb.write(t_row, t_col + 3, m_time, self.style)
                t_row = t_row + 1
        try:
            sheet.save(self.xlsxname)
        except:
            print("Wangyi Save Error = 6")


    def getBusiness(self): #市场资讯 获取两页
        bu_url = 'http://money.163.com/special/00251LR5/cpznList.html'
        bu_url2 = 'http://money.163.com/special/00251LR5/cpznList_02.html' #第二页
        
        bu_data1 = requests.get(bu_url, headers=headers)
        soup1 = BeautifulSoup(bu_data1.text, "lxml")

        bu_data2 = requests.get(bu_url2, headers=headers)
        soup2 = BeautifulSoup(bu_data2.text, "lxml")

        if_write = True
        self.get_bu(soup1, if_write)
        if_write = False
        self.get_bu(soup2, if_write)


    def get_Indu(self, soup, if_write):
        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[0]
        t_row = table.nrows  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet(0)
        if if_write == True:
            wb.write(t_row + 1, t_col, "行业板块", self.style_head)
            wb.write(t_row + 2, t_col, "新闻标题", self.style_head)
            wb.write(t_row + 2, t_col + 1, "新闻链接", self.style_head)
            wb.write(t_row + 2, t_col + 2, "新闻简介", self.style_head)
            wb.write(t_row + 2, t_col + 3, "新闻时间", self.style_head)
            t_row = t_row + 3

        datalist = soup.find_all(class_="col_l")
        for Newslist in datalist:
            News = Newslist.find_all(class_="list_item clearfix")
            for newlist in News:
                news = newlist.find_all(class_="item_top")
                for new in news:
                    m_new = new.select('h2 a')
                    m_url = m_new[0]['href']
                    m_title = m_new[0].get_text()
                    m_new2 = new.select('p span')
                    m_time = m_new2[0].get_text()
                    wb.write(t_row, t_col, m_title, self.style)
                    wb.write(t_row, t_col + 1, m_url, self.style)
                    wb.write(t_row, t_col + 3, m_time, self.style)
                    t_row = t_row + 1
        try:
            sheet.save(self.xlsxname)
        except Exception:
            print("Wangyi Save Error = 7")

    def getIndustry(self): #行业资讯 前两页
        url = 'http://money.163.com/special/00251LJV/hyyj.html'
        url2 = 'http://money.163.com/special/00251LJV/hyyj_02.html'

        Industry_data1 = requests.get(url, headers=headers)
        soup1 = BeautifulSoup(Industry_data1.text, "lxml")
        Industry_data2 = requests.get(url2, headers=headers)
        soup2 = BeautifulSoup(Industry_data2.text, "lxml")
        if_write = True
        self.get_Indu(soup1, if_write)
        if_write = False
        self.get_Indu(soup2, if_write)


    def main(self, file_name):
        Wy = WangYi(file_name)
        Wy.Style()
        Wy.getTopNew()
        Wy.getlist2()
        #stock
        Wy.getstock()
        Wy.getindex()  # 主页原创栏目右边
        Wy.getBusiness()
        Wy.getIndustry()
