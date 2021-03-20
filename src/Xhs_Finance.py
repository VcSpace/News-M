import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class XinHuaNet(object):
    def __init__(self):
        pass

    def request(self):
        self.url = 'http://www.xinhuanet.com/fortunepro/'
        self.data = requests.get(self.url, headers=headers)
        self.data.encoding = "utf-8"
        self.soup = BeautifulSoup(self.data.text, "lxml")


    def getTopNew(self):
        wb = load_workbook(self.xlsxname)
        sheet = wb.create_sheet("Xhs")
        t_row = 1
        t_col = 1

        sheet.cell(row=t_row, column=t_col, value="新华社财经")
        t_row = t_row + 1
        sheet.cell(row=t_row, column=t_col, value="新闻标题")
        sheet.cell(row=t_row, column=t_col + 1, value="新闻链接")
        sheet.cell(row=t_row, column=t_col + 2, value="新闻简介")
        sheet.cell(row=t_row, column=t_col + 3, value="新闻时间")
        t_row = t_row + 1

        datalist = self.soup.find_all(class_='infoList clearfix')
        for newlist in datalist:
            news = newlist.find_all('a')
            for m_new in news:
                m_href = m_new['href']
                m_title = m_new.get_text()
                sheet.cell(row=t_row, column=t_col, value=m_title)
                sheet.cell(row=t_row, column=t_col + 1, value=m_href)
                t_row = t_row + 1

        try:
            wb.save(self.xlsxname)
        except Exception:
            print("Xhs Save Error = 1")

    def main(self, file_name):
        self.xlsxname = file_name
        Xhs.request()
        Xhs.getTopNew()


Xhs = XinHuaNet()
