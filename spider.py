#-*- coding=utf-8 -*-
#@time: 2021/11/1 12:56
#@author: 陈立
#@file: spider.py
#@Software: PyCharm


from bs4 import BeautifulSoup              #网页解析，获取数据
import re                #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL，获取网页数据
import xlwt              #进行excel操作
import sqlite3           #进行SQLite数据库操作



def main():
    baseurl="https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    # saveData(savepath)
    # askURL(baseurl)




#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)  #调用获取页面信息的函数，10次
        html = askURL(url)    #保存获取到的网页源码

    # 2.逐一解析数据
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all()    #查找符合要求的字符串， 
    return datalist




#得到一个指定url的网页内容
def askURL(url):
    head = {   #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent":"Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 94.0.4606.54Safari / 537.36"
    }          #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器我们可以接收什么水平的文件类型）

    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)   #判断e这个对象里面是否包含code这个属性
        if hasattr(e,"reason"):
            print(e.reason)

    return html



#保存数据
def saveData(savepath):
    print("save...")

if __name__=="__main__":
    main()
