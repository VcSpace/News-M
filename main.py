from Wy_Finance import WangYi
from Ths_Finance import TongHuaShun
from Jrj_Finance import JinRongJie
from Xq_Community import XueQiu
from Self_Stock import SelfStock
import os, shutil
import time
import platform


def get_platform():
    sys = platform.system()
    if sys == "Windows":
        return True
    elif sys == "Linux":
        return False

def file_move(platform):
    if platform:
        win_filemove()
    else:
        linux_filemove()

def linux_filemove():
    path = "./Finance/"
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)

    lin_News()
    lin_History()

def lin_News():
    path = "./Finance/News/"
    filename = "./News_Finance.xlsx"
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime())  # year-month-day-hour-minute
    path2 = path + "/" +"闻讯__" + filetime + ".xlsx"
    shutil.move(filename, path2)

def lin_History():
    path = "./Finance/History/"
    file_name = "./Main_History.xlsx"
    isExists = os.path.exists(path + "闻讯_主力资金历史.xlsx")
    isExists2 = os.path.exists(path)
    if not isExists:
        if not isExists2:
            os.mkdir(path)
        #filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime())  # year-month-day-hour-minute
        path2 = path + "闻讯_主力资金历史" + ".xlsx"
        shutil.move(file_name, path2)


def win_filemove():
    desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
    path = desktop_path + "\\Finance\\"
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)

    win_News()
    win_History()

def win_News():
    desktop_path = os.path.join(os.path.expanduser('~'),"Desktop") #获取桌面路径
    filename = desktop_path + "\\Finance\\News_Finance.xlsx"
    path = desktop_path +"\\Finance\\News\\"

    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime()) #year-month-day-hour-minute
    path2 = path + "闻讯__" + filetime + ".xlsx"
    shutil.move(filename, path2)

def win_History():
    desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
    filename = desktop_path + "\\Finance\\Main_History.xlsx"
    path = desktop_path + "\\Finance\\History\\"
    isExists = os.path.exists(path + "闻讯_主力资金历史.xlsx")
    isExists2 = os.path.exists(path)
    if not isExists:
        if not isExists2:
            os.mkdir(path)
        # filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime())  # year-month-day-hour-minute
        path2 = path + "闻讯_主力资金历史" + ".xlsx"
        shutil.move(filename, path2)

#----------------------------
"""
上部分为移动文件、重命名操作 可以无视
"""

def Wy(filename):
    Wy = WangYi(filename)
    Wy.main(filename)

def THS(filename):
    Ths = TongHuaShun(filename)
    Ths.main(filename)

def JRJ(filename):
    Jrj = JinRongJie(filename)
    Jrj.main(filename)

def Xq(filename):
    Xq = XueQiu(filename)
    Xq.main(filename)

def Stock(filename):
    Stock = SelfStock(filename)
    Stock.main(filename)

def get_News(platform, win_file, lin_file):
    if platform:
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
        dir = os.path.exists(desktop_path + "\\Finance")
        if not dir:
            os.mkdir(dir)
        Wy(win_file)
        THS(win_file)
        JRJ(win_file)
        Stock(win_file)
    else:
        Wy(lin_file)
        THS(lin_file)
        JRJ(lin_file)
        Stock(lin_file)


if __name__ == '__main__':
    desktop_path = os.path.join(os.path.expanduser('~'),"Desktop") #获取桌面路径
    win_file = desktop_path + "\\Finance\\News_Finance.xlsx"
    linux_file = "./News_Finance.xlsx"

    m_platform = get_platform() #判断系统 win/linux 设置配置
    get_News(m_platform, win_file, linux_file)
    file_move(m_platform)

    print("操作完成")
