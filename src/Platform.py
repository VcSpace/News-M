import platform
import os
import shutil
import time

class Files(object):
    def __init__(self):
       pass

    def get_platform(self):
        sys = platform.system()
        if sys == "Windows":
            return True
        elif sys == "Linux":
            return False

    def file_move(self, platform):
        if platform:
            self.win_filemove()
        else:
            self.linux_filemove()

    def linux_filemove(self):
        path = "./Finance/"
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
        self.lin_News()
        self.lin_History()

    def lin_News(self):
        path = "./Finance/News/"
        filename = "./News_Finance.xlsx"
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
        filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime())  # year-month-day-hour-minute
        path2 = path + "/" +"闻讯__" + filetime + ".xlsx"
        shutil.move(filename, path2)

    def lin_History(self):
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

    def win_filemove(self):
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
        path = desktop_path + "\\Finance\\"
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)

        self.win_News()
        self.win_History()

    def win_News(self):
        desktop_path = os.path.join(os.path.expanduser('~'),"Desktop") #获取桌面路径
        filename = desktop_path + "\\Finance\\News_Finance.xlsx"
        path = desktop_path +"\\Finance\\News\\"

        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
        filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime()) #year-month-day-hour-minute
        path2 = path + "闻讯__" + filetime + ".xlsx"
        shutil.move(filename, path2)

    def win_History(self):
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

    def linux_filename(self):
        linux_file = "./News_Finance.xlsx"

    def win_filename(self):
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
        win_file = desktop_path + "\\Finance\\News_Finance.xlsx"

    def pause(self):
        os.system('pause')

    def win_mkdir(self):
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
        dir = os.path.exists(desktop_path + "\\Finance")
        if not dir:
            os.mkdir(dir)