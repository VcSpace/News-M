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
            self.win_News()
        else:
            self.lin_News()
            
    def lin_News(self):
        path = "./Finance/News/"
        filename = "./News_Finance.xlsx"
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
        #filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime())  # year-month-day-hour-minute
        filetime = time.strftime("%Y_%m_%d_%H", time.localtime())  # year-month-day-hour-minute
        path2 = path + "闻讯__" + filetime + "时.xlsx"
        shutil.move(filename, path2)

    def win_News(self):
        desktop_path = os.path.join(os.path.expanduser('~'),"Desktop") #获取桌面路径
        filename = desktop_path + "\\Finance\\News_Finance.xlsx"
        path = desktop_path +"\\Finance\\News\\"

        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
        #filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime()) #year-month-day-hour-minute
        filetime = time.strftime("%Y_%m_%d_%H", time.localtime()) #year-month-day-hour-minute
        path2 = path + "闻讯__" + filetime + "时.xlsx"
        shutil.move(filename, path2)


    def linux_filename(self):
        path = "./Finance/"
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)
        # self.lin_History()
        linux_file = "./News_Finance.xlsx"
        return linux_file

    def win_filename(self):
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
        path = desktop_path + "\\Finance\\"
        isExists = os.path.exists(path)
        if not isExists:
            os.mkdir(path)

        win_file = desktop_path + "\\Finance\\News_Finance.xlsx"
        return win_file

    def pause(self):
        os.system('pause')

    """
    def win_mkdir(self):
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
        dir = os.path.exists(desktop_path + "\\Finance")
        if not dir:
            os.mkdir(dir)
    """
    def getwinfile(self):
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
        filename = desktop_path + "\\Finance\\News_Finance.xlsx"
        path = desktop_path + "\\Finance\\News\\"
        # filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime()) #year-month-day-hour-minute
        filetime = time.strftime("%Y_%m_%d", time.localtime())  # year-month-day-hour-minute
        path2 = path + "闻讯__" + filetime + ".xlsx"
        return path2

    def getlinfile(self):
        path = "./Finance/News/"
        filename = "./News_Finance.xlsx"
        isExists = os.path.exists(path)
        # filetime = time.strftime("%Y_%m_%d_%H_%M", time.localtime())  # year-month-day-hour-minute
        filetime = time.strftime("%Y_%m_%d", time.localtime())  # year-month-day-hour-minute
        path2 = path + "闻讯__" + filetime + ".xlsx"
        return path2


    def getfilename(self):
        if self.get_platform() == True:
            return self.getwinfile()
        else:
            return self.getlinfile()

    def filename(self):
        filetime = time.strftime("%Y_%m_%d", time.localtime())  # year-month-day-hour-minute
        path2 = "闻讯__" + filetime + ".xlsx"
        return path2

    def getwinpath(self):
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")  # 获取桌面路径
        path = desktop_path + "\\Finance\\" + " \\"
        return path

    def getlinpath(self):
        path = "./Finance/" + " /"
        return path

    def getpath(self):
        if self.get_platform() == True:
            return self.getwinpath()
        else:
            return self.getlinpath()


pt = Files()
