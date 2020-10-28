import requests
from bs4 import BeautifulSoup
import os
import xlrd, xlwt

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
}

class WangYi(object):
    def __init__(self):
        self.url = 'https://money.163.com/'
        self.data = requests.get(self.url, headers=headers)

    def getTopNew(self):
        print("要闻 ")
        soup = BeautifulSoup(self.data.text, "lxml")
        datalist = soup.select("ul li h2")
        #print(datalist)
        #datalist = soup.find_all(class_="topnews_nlist topnews_nlist1")
        #print(datalist)

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

        wsheet.write(0, 0, u'新闻标题', style)
        wsheet.write(0, 1, u'新闻链接', style)
        wsheet.write(0, 2, u'新闻时间', style)
        wsheet.write(0, 3, u'内容简介', style)

        t_row = 1
        t_col = 0
        for li in datalist:
            url = li.find('a')['href']
            title = li.get_text()
            wsheet.write(t_row, t_col, title)
            wsheet.write(t_row, t_col + 1, url)
            t_row = t_row + 1
        try:
            wbook.save('C:\\Users\\Vcvc\\Desktop\\' + 'Wangyi.xlsx')
        except:
            print('Save error')
        else:
            print('excel save')



if __name__ == '__main__':
    Wy = WangYi()
    if not os.path.exists("./WangYiNews"):
        os.mkdir("./WangYiNews")
    Wy.getTopNew()
    """
    try:
        Wy.getTopNew()
    except Exception:
        print("获取TopNew失败")
    """
