import threading
from src.Platform import pt
from src.Wy_Finance import Wy
from src.Ths_Finance import Ths
from src.Jrj_Finance import Jrj
from src.Fh_Finance import Fh
from src.East_Finance import Ew
from src.CCTV_News import CCTV
from src.Sina_Finance import Sina
from src.Xhs_Finance import Xhs
from src.Sg_Finance import Sg
import src.Baidu_upload

def get_News(platform, filename, debug):
    #debug True开启
    if debug:
        Wy.create_file(filename)
        return
    Wy.main(filename)
    t1 = threading.Thread(target=CCTV.main, args=())
    t1.start()
    Xhs.main(filename)
    Ths.main(filename)
    Jrj.main(filename)
    Fh.main(filename)
    Ew.main(filename)
    Sina.main(filename)
    Sg.main(filename)
    t1.join()

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
        
        
"""
#服务器定时运行
#添加库: time logging random
#https://blog.csdn.net/ainivip/article/details/106296599
if __name__ == '__main__':
    while True:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        log_time = time.strftime("%Y_%m_%d", time.localtime())  # 刷新
        logfile = "./" + log_time + ".log"
        fh = logging.FileHandler(logfile,mode='w')
        fh.setLevel(logging.INFO)
        
        while True:
            rnum = random.randint(60, 100);
            formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            time_now = time.strftime("%H", time.localtime())  # 刷新
            if time_now == "21" or time_now == "10": # 设置要执行的时间
                start()
                logger.info("sleep(20000) start news_d")
                time.sleep(4000 + rnum)
            elif time_now == "00":
                logger.info("new day, log end")
                logger.removeHandler(fh)
                time.sleep(3600 + rnum)
                break
            else:
                logger.info("wait sleep(600)")
                time.sleep(600 + rnum)
"""
