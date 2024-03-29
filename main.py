import threading
import time
import logging
import random
import os

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
from src.Sg_Finance import Sg
from src.Tzj_Finance import Tzj
import src.Baidu_upload

def get_News(platform, filename, debug):
    #debug True开启
    if debug:
        Wy.create_file(filename)
        CCTV.main()
        return
    Wy.main(filename) 
    # t1 = threading.Thread(target=CCTV.main, args=()) #新闻联播文字版获取默认关闭，经常失效，失效后不再更新
    # t2 = threading.Thread(target=Stock.main, args=(filename,)) #个股处理版本默认关闭，使用先在Code.txt添加代码+名称，失效不再更新
    # t1.start()
    # t2.start()
    Xhs.main(filename)
    Ths.main(filename)
    Jrj.main(filename)
    # Fh.main(filename)#接口失效
    Ew.main(filename)
    Sina.main(filename)
    Tzj.main(filename)
    Sg.main(filename)
    # t1.join()
    # t2.join()

def get_filename(platform):
    if platform == True:
        win_file = pt.win_filename()
        return win_file
    else:
        linux_file = pt.linux_filename()
        return linux_file

if __name__ == '__main__':
    Debug = False
    m_platform = pt.get_platform() #判断系统
    filename = get_filename(m_platform)
    get_News(m_platform, filename, Debug) #获取信息

    pt.file_move(m_platform) #文件移动 重命名操作

    """
    授权步骤
    命令行bypy info || python -m bypy info || python3 -m bypy info
    打开链接-登陆-授权
    复制授权码
    粘贴到命令行-enter
    """
    bd_flag = False #改为True开启
    if bd_flag == False or Debug == True:
        print("如果需要上传到云盘备份 请自行开启bd.main \n")
    else:
        Bd = src.Baidu_upload.Baidu()
        Bd.main()

    print("操作完成")

    if m_platform == True:
        pt.pause()
