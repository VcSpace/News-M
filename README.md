# 闻讯 | News-M

![https://img.shields.io/github/workflow/status/VcSpace/News-M/newsci](https://img.shields.io/github/workflow/status/VcSpace/News-M/newsci) ![https://img.shields.io/badge/platform-Linux--64%20%7C%20Macosx%20%7C%20Win--64-blue](https://img.shields.io/badge/platform-Linux%20%7C%20Macos%20%7C%20Windows-blue) ![https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue](https://img.shields.io/badge/python-v3-blue) ![https://img.shields.io/github/license/VcSpace/News-M?color=blue](https://img.shields.io/github/license/VcSpace/News-M?color=blue) ![https://img.shields.io/github/stars/VcSpace/News-M?style=social](https://img.shields.io/github/stars/VcSpace/News-M?style=social)

**闻讯——用于采集财经新闻网站新闻, 将数据聚合、归类并写入表格之中。**

**News-M--Get news from mainstream financial news websites, aggregate, categorize, and write data into tables.**
 
---

## 更新 | Update

**2022-02-13: cctv新闻文字版暂时又正常了，缺失的可以简单修改代码手动补全。**

**分支项目：News-E: [https://github.com/VcSpace/News-E](https://github.com/VcSpace/News-E), 外网财经新闻获取，了解世界经济。**

---

## 数据来源 | Data

**网易财经、同花顺财经、金融界财经、凤凰财经、东方财富、新浪财经、新华网财经、松果财经、新闻联播文字版、投资界, 数据会生成表格存放在Finance文件夹中**

**NetEase Finance and economics, flush finance and economics, finance and economics in financial circles, Phoenix finance and economics, Oriental Fortune, sina finance and economics, Xinhuanet finance and economics, pinecone finance and economics, news broadcast text version and investment circles. The data will be generated into tables and stored in the finance folder**

---

## 运行程序 ｜ Run

```python
#Run
pip install -r requirements.txt
python3 main.py
```

**Windows新闻文件生成在桌面, Linux/Macos生成在运行目录下**

**Windows system is generated on the desktop, Linux/Macos is generated in the running directory**

**视频展示 | Video display: [https://www.bilibili.com/video/BV1dK4y1M7d4](https://www.bilibili.com/video/BV1dK4y1M7d4)**

**使用教程 | Tutorial: [https://6923403.github.io/post/news_wps](https://6923403.github.io/post/news_wps)**

- 更多设置, 请查看教程

- More settings， check out the tutorial
 
---

## 跨平台 | Cross-Plateform

**实机测试:**

**Running in real environment**

- **Windows7 + python3.7**

- **Ubuntu20.04 + python3.8**

- **Macos11.4 + python3.9**

---

## 关于 | About

**提取财经新闻标题、链接进行整合排列写入表格，省去了人眼识别->大脑检索->点击鼠标->打开/关闭的繁琐步骤, 我每日会大约花费一小时时间用来获取最新的新闻资讯，效率极低。本项目提升获取效率，缩短了花费在新闻获取的时间。**

**Extracting the financial news headlines and links for integration and arrangement and writing them into the table eliminates the complicated steps of searching the website, opening the web page, viewing the title, opening the web page, closing the web page and continuing to view the next one. In the past, it took one hour to get up early to watch the news, but now it can be done in 10 minutes.**

**本项目主要抓取财经金融类新闻、资讯取得的数据仅供参考。**

**This project mainly captures financial and financial news, information. The data obtained is for reference only.**

```
此外本项目分为M,D,E 三个分支，D分支主要用于股票相关(只有大A，港股美股没有)，所以暂时不打算开放。未来准备加入ai分析(在研究...)，利用D分支的数据做一个数据分析、趋势判断，想做个萝卜投研这个类型的站点.(https://robo.datayes.com/v2/landing/indicator_library)。个人能力有限，不知道有没有会看到这里的，有想法、有能力的可以issues留个言。

另外，我目前主要投入美股(苹果\微软\谷歌\Meta\英伟达\阿斯麦)，新闻目前很少看国内，所以后续大概维护为主，但是会对内容质量以及用取得的数据做一些辅助工作，目前暂时没想好，也没有时间。 某软体动物真的没意思。
```

---

## 开源协议 | License

``MIT  License``

---

## 编辑器 | IDE 

**[Use Pycharm](https://www.jetbrains.com/pycharm/)**

