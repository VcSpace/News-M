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
    t1 = threading.Thread(target=CCTV.main, args=())
    # t2 = threading.Thread(target=Stock.main, args=(filename,)) #进入维护待更新状态
    t1.start()
    # t2.start()
    Xhs.main(filename)
    Ths.main(filename)
    Jrj.main(filename)
    Fh.main(filename)
    Ew.main(filename)
    Sina.main(filename)
    Tzj.main(filename)
    Sg.main(filename)
    t1.join()
    # t2.join()

def get_filename(platform):
    if platform == True:
        win_file = pt.win_filename()
        return win_file
    else:
        linux_file = pt.linux_filename()
        return linux_file

def start():
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
    bd_flag = True #改为True开启
    if bd_flag == False or Debug == True:
        print("如果需要上传到云盘备份 请自行开启bd.main \n")
    else:
        Bd = src.Baidu_upload.Baidu()
        Bd.main()

    print("操作完成")

    if m_platform == True:
        pt.pause()


if __name__ == '__main__':
    print('start')

    path = "./logs/"
    isExists = os.path.exists(path)   
    if not isExists:
        os.mkdir(path)
    while True:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        log_time = time.strftime("%Y_%m_%d", time.localtime())  # 刷新
        logfile = path + log_time + ".log"
        if os.path.exists(logfile):
            log_time = time.strftime("%Y_%m_%d_%H", time.localtime())  # 另创建
            logfile = path + log_time + "时.log"
        fh = logging.FileHandler(logfile,mode='w')
        fh.setLevel(logging.INFO)
        
        while True:
            formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            time_now = time.strftime("%H", time.localtime())  # 刷新
            if time_now == "11" or time_now == "16" or time_now == "21": # 设置要执行的时间
                logger.info("New-D Start")
                start()
                logger.info("sleep(4567) start news_d")
                time.sleep(4567)
            elif time_now == "00":
                logger.info("new day, log end")
                logger.removeHandler(fh)
                time.sleep(4567)
                break
            else:
                logger.info("wait sleep(1234)")
                time.sleep(1234)