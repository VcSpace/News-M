import requests
import json
import os
import time

"""
POST https://www.en
tobit.cn/trending/top/getWeiboRankSearch.do HTTP/1.1
Host: www.entobit.cn
Connection: keep-alive
Content-Length: 33
sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"
Accept: application/json, text/plain, */*
Content-Type: application/x-www-form-urlencoded
sec-ch-ua-mobile: ?0
type: restful
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: https://www.entobit.cn
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.ent
obit.cn/hot-search/nav/home?accessToken=Cjr8dOf3BVcz6kQELQ24/SHCztOETa%2BGJuB%2BR4c2SaWErDW6BR7ZBuKo5idM1TWHQ2YHNf6GjPn6Vxb971zAPw==&bindPhone=false&isIos=&isWx=
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9

keyword=%E7%BE%8E%E5%85%83&from=1

HTTP/1.1 200 OK
Server: nginx/1.18.0
Date: Thu, 11 May 2023 08:52:42 GMT
Content-Type: application/json;charset=UTF-8
Content-Length: 6209
Connection: keep-alive

{"rows":[{"duration":9840,"searchNums":29164,"keywords":"莫兰特损失4000万美元","updateTime":1683794940,"type":"realTimeHotSpots","topRanking":21,"url":"https://s.weibo.com/weibo?q=%23%E8%8E%AB%E5%85%B0%E7%89%B9%E6%8D%9F%E5%A4%B14000%E4%B8%87%E7%BE%8E%E5%85%83%23","firstRankingTime":1683785700},{"duration":82260,"searchNums":1494363,"keywords":"特朗普性侵罪成 向女作家赔500万美元","updateTime":1683761340,"type":"toutiao","topRanking":1,"url":"https://m.toutiao.com/search/?keyword=特朗普性侵罪成 向女作家赔500万美元&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683675000},{"duration":3720,"searchNums":37860,"keywords":"美国宣布再向乌提供12亿美元军援","updateTime":1683737160,"type":"toutiao","topRanking":35,"url":"https://m.toutiao.com/search/?keyword=美国宣布再向乌提供12亿美元军援&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683733140},{"duration":6480,"searchNums":283486,"keywords":"外媒：“去美元化”已成当下趋势","updateTime":1683712200,"type":"toutiao","topRanking":8,"url":"https://m.toutiao.com/search/?keyword=外媒：“去美元化”已成当下趋势&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683700200},{"duration":12180,"searchNums":8581651,"keywords":"美将向乌提供12亿美元军事援助","updateTime":1683676080,"type":"kwai","topRanking":1,"url":"","firstRankingTime":1683614220},{"duration":18660,"searchNums":22312,"keywords":"崩铁希儿吸金近三千万美元","updateTime":1683606420,"type":"realTimeHotSpots","topRanking":21,"url":"https://s.weibo.com/weibo?q=%23%E5%B4%A9%E9%93%81%E5%B8%8C%E5%84%BF%E5%90%B8%E9%87%91%E8%BF%91%E4%B8%89%E5%8D%83%E4%B8%87%E7%BE%8E%E5%85%83%23","firstRankingTime":1683587820},{"duration":2460,"searchNums":164917,"keywords":"沙特将向苏丹提供价值1亿美元援助","updateTime":1683527040,"type":"toutiao","topRanking":31,"url":"https://m.toutiao.com/search/?keyword=沙特将向苏丹提供价值1亿美元援助&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683517140},{"duration":5100,"searchNums":2465723,"keywords":"美媒:好莱坞编剧罢工损失超100亿美元","updateTime":1683526800,"type":"baidu","topRanking":6,"url":"https://www.baidu.com/s?wd=%E7%BE%8E%E5%AA%92%3A%E5%A5%BD%E8%8E%B1%E5%9D%9E%E7%BC%96%E5%89%A7%E7%BD%A2%E5%B7%A5%E6%8D%9F%E5%A4%B1%E8%B6%85100%E4%BA%BF%E7%BE%8E%E5%85%83&amp;sa=fyb_news&amp;rsv_dl=fyb_news","firstRankingTime":1683506100},{"duration":58020,"searchNums":2320820,"keywords":"截至4月末外汇储备规模32048亿美元","updateTime":1683512820,"type":"toutiao","topRanking":2,"url":"https://m.toutiao.com/search/?keyword=截至4月末外汇储备规模32048亿美元&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683429660},{"duration":11160,"searchNums":52850,"keywords":"2023年全球票房破100亿美元","updateTime":1683455700,"type":"toutiao","topRanking":8,"url":"https://m.toutiao.com/search/?keyword=2023年全球票房破100亿美元&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683442080},{"duration":20520,"searchNums":24139,"keywords":"国际奥委会向中国奥委会捐赠1040万美元","updateTime":1683455640,"type":"realTimeHotSpots","topRanking":21,"url":"https://s.weibo.com/weibo?q=%23%E5%9B%BD%E9%99%85%E5%A5%A5%E5%A7%94%E4%BC%9A%E5%90%91%E4%B8%AD%E5%9B%BD%E5%A5%A5%E5%A7%94%E4%BC%9A%E6%8D%90%E8%B5%A01040%E4%B8%87%E7%BE%8E%E5%85%83%23","firstRankingTime":1683434700},{"duration":480,"searchNums":137737,"keywords":"巴菲特：美元未来不一定是储备货币","updateTime":1683436680,"type":"toutiao","topRanking":43,"url":"https://m.toutiao.com/search/?keyword=巴菲特：美元未来不一定是储备货币&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683436260},{"duration":11340,"searchNums":6937663,"keywords":"拜登政府对台提供5亿美元军援","updateTime":1683435360,"type":"kwai","topRanking":6,"url":"","firstRankingTime":1683359460},{"duration":660,"searchNums":21969,"keywords":"2023全球票房破100亿美元","updateTime":1683432660,"type":"realTimeHotSpots","topRanking":63,"url":"https://s.weibo.com/weibo?q=%232023%E5%85%A8%E7%90%83%E7%A5%A8%E6%88%BF%E7%A0%B4100%E4%BA%BF%E7%BE%8E%E5%85%83%23","firstRankingTime":1683430980},{"duration":41580,"searchNums":206584,"keywords":"中国奥委会获捐1040万美元","updateTime":1683418440,"type":"toutiao","topRanking":1,"url":"https://m.toutiao.com/search/?keyword=中国奥委会获捐1040万美元&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683376920},{"duration":28800,"searchNums":41653,"keywords":"外媒：美拟向台湾提供价值5亿美元武器","updateTime":1683416400,"type":"toutiao","topRanking":18,"url":"https://m.toutiao.com/search/?keyword=外媒：美拟向台湾提供价值5亿美元武器&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683350700},{"duration":2820,"searchNums":18464,"keywords":"4月中国游戏厂商全球吸金20亿美元","updateTime":1683368460,"type":"realTimeHotSpots","topRanking":63,"url":"https://s.weibo.com/weibo?q=%234%E6%9C%88%E4%B8%AD%E5%9B%BD%E6%B8%B8%E6%88%8F%E5%8E%82%E5%95%86%E5%85%A8%E7%90%83%E5%90%B8%E9%87%9120%E4%BA%BF%E7%BE%8E%E5%85%83%23","firstRankingTime":1683364500},{"duration":2700,"searchNums":0,"keywords":"Intel净亏损28亿美元","updateTime":1683356400,"type":"bilibili","topRanking":19,"url":"https://search.bilibili.com/all?keyword=Intel%E5%87%80%E4%BA%8F%E6%8D%9F28%E4%BA%BF%E7%BE%8E%E5%85%83&from_source=webtop_search&spm_id_from=333.851","firstRankingTime":1683353700},{"duration":2880,"searchNums":7215648,"keywords":"各国放弃美元怎么办","updateTime":1683355320,"type":"kwai","topRanking":33,"url":"","firstRankingTime":1683348540},{"duration":1440,"searchNums":295947,"keywords":"是否担心多国去美元化？白宫回应","updateTime":1683354180,"type":"toutiao","topRanking":19,"url":"https://m.toutiao.com/search/?keyword=是否担心多国去美元化？白宫回应&pd=synthesis&source=trending_list&traffic_source=","firstRankingTime":1683350160}],"total":3119}
"""
session = requests.Session()

headers = {
    'Host': 'www.ent'
            'obit.cn',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '33',
    # 'Referer': 'https://www.entobit.cn/hot-search/nav/home?accessToken=Cjr8dOf3BVcz6kQELQ24/SHCztOETa%2BGJuB%2BR4c2SaWErDW6BR7ZBuKo5idM1TWHQ2YHNf6GjPn6Vxb971zAPw==&bindPhone=false&isIos=&isWx=',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
def request(text, num):
    url = 'https://www.ento' \
          'bit.cn/trending/top/getWeiboRankSearch.do'
    key = {
        'keyword': '{0}'.format(text),
        'from': '{0}'.format(num)
    }

    for _ in range(3):
        try:
            res = session.post(url, headers=headers, data=key, timeout=(20, 30))
            if res.status_code == 200:
                if res.text == "{\"rows\":[],\"total\":23}":
                    print("time 10000")
                    time.sleep(10000)
                with open("./{0}.txt".format(text), "a") as file:
                    file.write(res.text + '\n')
                    return True
        except Exception as e:
            print(e)

    return False


if __name__ == '__main__':
    num = 1
    text = 'NFT'
    while True:
        print("cur = ", num)
        ret = request(text, num)
        time.sleep(5)
        if ret == False:
            print("error: ", num)
            time.sleep(10)

        num = num + 1
