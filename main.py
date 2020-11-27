from src.Wy_Finance import WangYi
from src.Ths_Finance import TongHuaShun
from src.Jrj_Finance import JinRongJie
from src.Self_Stock import SelfStock
from src.Platform import Files

def Wy(filename):
    Wy = WangYi(filename)
    Wy.main(filename)

def THS(filename):
    Ths = TongHuaShun(filename)
    Ths.main(filename)

def JRJ(filename):
    Jrj = JinRongJie(filename)
    Jrj.main(filename)

def Stock(filename):
    Stock = SelfStock(filename)
    Stock.main(filename)

def get_News(platform, win_file, lin_file):
    if platform:
        #pt.win_mkdir() #win下创建Finance文件夹
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
    pt = Files()
    win_file = pt.win_filename()
    linux_file = pt.linux_filename()

    m_platform = pt.get_platform() #判断系统
    get_News(m_platform, win_file, linux_file) #获取信息

    pt.file_move(m_platform) #文件移动 重命名操作

    print("操作完成")

    if m_platform == True:
        pt.pause()
