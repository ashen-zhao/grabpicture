#coding=utf-8
import urllib
import re
import os
import datetime
import urllib2

HOST = 'https://image.baidu.com'
I = 0
def getRelevantsearch(url,keyword):
    data = getHtml(url)
    reg = r'<a.+?class="pull-rs".+?title=".+?%s.+?".+?href="(.+?)".+?>+?'%keyword
    urlre = re.compile(reg)
    urllist = re.findall(urlre, data)
    links = []
    for url in urllist:
        url = HOST + url
        links.append(url)
    return links

def getImg(data,keyword):
    reg = r'"thumbURL":"(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,data)
    exist = os.path.exists(keyword)
    index = 0
    global I
    if not exist:
        os.mkdir(keyword)
    for imgurl in imglist:
        print '%s.jpg' % I
        urllib.urlretrieve(imgurl,'./%s/%s.jpg' % (keyword,I))
        I+=1

def getHtml(url):
    page = urllib.urlopen(url)
    data = page.read()
    return data

def main():

    str = raw_input("输入要抓取图片的关键词：")
    links = getRelevantsearch(HOST + "/search/index?tn=baiduimage&word=" + str, str)
    data = getHtml(HOST + "/search/index?tn=baiduimage&word=" + str)
    getImg(data, str)
    for link in links:
        data = getHtml(link)
        getImg(data, str)


if __name__ == '__main__':
    main()
