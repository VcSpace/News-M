import os
import requests
import json
from src.Platform import pt
from bypy import ByPy
bp = ByPy()

class Baidu(object):
    def __init__(self):
        pass
        #print(bp.info())  # or whatever instance methods of ByPy class
        # 使用上传接口之前，请申请接入，申请地址为：https://pan.baidu.com/union/apply/

    # def get_token(self):
    #     #用不到
    #     url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}".format(self.AppKey, self.SecretKey)
    #     # 获取token
    #     res = requests.get(url).text
    #     data = json.loads(res)  # 将json格式转换为字典格式
    #     self.access_token = data['access_token']
    #     self.filename = pt.filename()

    def upload(self):
        path = pt.getpath()
        print("正在同步备份文件，如果文件过多 请耐心等待")
        #re: https://www.jianshu.com/p/19ddb60e2b22
        cmd = 'bypy syncup ' + path + " /"
        print("上传完成: ", os.system(cmd))

    def main(self):
        Bd.upload() #bypy 把当前目录同步到云盘


Bd = Baidu()