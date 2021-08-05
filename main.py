import threading
from src.Platform import pt
from src.Wy_Finance import Wy
from src.Ths_Finance import Ths
from src.Jrj_Finance import Jrj
from src.Fh_Finance import Fh
from src.East_Finance import Ew
from src.Self_Stock import Stock
from src.CCTV_News import CCTV
from src.Sina_Finance import Sina
from src.Xhs_Finance import Xhs
from src.Yh_Finance import Yh
from src.Sg_Finance import Sg


def get_News(platform, filename, debug):
    #debug True开启
    if debug:
        Wy.create_file(filename)
        return
    Wy.main(filename)
    t1 = threading.Thread(target=CCTV.main, args=())
    t2 = threading.Thread(target=Stock.main, args=(filename,))
    t1.start()
    t2.start()
    Xhs.main(filename)
    Ths.main(filename)
    Jrj.main(filename)
    Fh.main(filename)
    Ew.main(filename)
    Sina.main(filename)
    Sg.main(filename)
    t1.join()
    t2.join()

def get_filename(platform):
    if m_platform == True:
        win_file = pt.win_filename()
        return win_file
    else:
        linux_file = pt.linux_filename()
        return linux_file

if __name__ == '__main__':
    debug = False
    m_platform = pt.get_platform() #判断系统
    filename = get_filename(m_platform)
    get_News(m_platform, filename, debug) #获取信息

    pt.file_move(m_platform) #文件移动 重命名操作

    print("操作完成")

    if m_platform == True:
        pt.pause()
