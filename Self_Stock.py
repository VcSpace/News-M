import requests
from bs4 import BeautifulSoup
import xlrd, xlwt
from xlutils.copy import copy
import json
from requests.cookies import RequestsCookieJar
import threading

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    #'Cookie': 'xqat=3e14cc861fdd960a5d84e7316165286b1bfeafe3;',
}

class SelfStock(object):
    threadLock = threading.Lock()
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

    def Deal_Xq_data(self, data, url, name):
        self.threadLock.acquire()

        xlsxin = xlrd.open_workbook(self.xlsxname, formatting_info=True)
        table = xlsxin.sheets()[0]
        t_row = table.nrows  # 已经使用多少行
        t_col = 0
        sheet = copy(xlsxin)
        wb = sheet.get_sheet_by_name(name)
        wb.write()

        data_json = data['data']
        data_items = data_json['items']
        data_mk = data_items[0]['market']
        data_quote = data_items[0]['quote']
        print(data_quote)

        m_status = data_mk['status']
        stock_code = data_quote['symbol']
        stock_name = data_quote['name']
        m_current = data_quote['current']
        m_percent = data_quote['percent'] #涨跌幅度
        m_chg = data_quote['chg'] #涨跌价格
        m_time = data_quote['timestamp']
        m_open = data_quote['open'] #开盘价
        m_yesclose = data_quote['last_close'] #昨收
        m_high = data_quote['high']
        m_low = data_quote['low']
        m_avg_price = data_quote['avg_price']
        m_amount = data_quote['amount'] #成交额
        m_turnover_rate = data_quote['turnover_rate'] #换手：0.74%
        m_amplitude = data_quote['amplitude'] #振幅
        m_market_capital = data_quote['market_capital'] #总市值
        m_total_shares = data_quote['total_shares'] #总股本
        m_float_shares = data_quote['float_shares'] #流通股
        m_high52w = data_quote['high52w'] #52周最高
        m_low52w = data_quote['low52w'] #52周最低
        m_limit_up = data_quote['limit_up'] #涨停
        m_limit_down = data_quote['limit_down'] #跌停
        m_volume_ratio = data_quote['volume_ratio'] #量比
        m_pe_ttm = data_quote['pe_ttm'] #市盈率
        m_pe_forecast = data_quote['pe_forecast'] #动态市盈率
        m_pe_lyr = data_quote['pe_lyr'] #静态市盈率
        m_pb = data_quote['pb'] #市净率
        m_profit = data_quote['profit'] #年报利润
        m_profit_four = data_quote['profit_four'] #也是利润 不清楚
        m_profit_forecast = data_quote['profit_forecast']

        try:
            sheet.save(self.xlsxname)
            self.threadLock.release()
        except Exception:
            print("Self_Stock Save Error = 2")
            self.threadLock.release()


    def get_SelfStock(self):
        url_list = list()
        name_list = list()
        with open("Code.txt", "r") as f:
            for line in f.readlines():
                m_line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                sep = '#'
                line = line.split(sep, 1)[0]
                if line != '':
                    #url = 'https://xueqiu.com/S/{}'.format(line)
                    url = 'https://stock.xueqiu.com/v5/stock/batch/quote.json?extend=detail&is_delay_ft=1&is_delay_hk=0&symbol={}'.format(line)
                    url_list.append(url)
                    name = m_line.split(sep)[1]
                    name_list.append(name)

        url = 'https://xueqiu.com'
        session = requests.session()
        session.get(url, headers=headers)
        name_list2 = name_list
        for url in url_list:
            for name in name_list2:
                name_list2.pop(0)
                resp = session.get(url, headers=headers)
                data = json.loads(resp.text)
                t1 = threading.Thread(target=self.Deal_Xq_data, args=(data, url, name))
                t1.start()
                t1.join()
                break
        try:
            print(1)
#            sheet.save(self.xlsxname)
        except Exception:
            print("Self_Stock Error = 1")

    def main(self, file_name):
        Stock = SelfStock(file_name)
        Stock.Style()
        Stock.get_SelfStock()
