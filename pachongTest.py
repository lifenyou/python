# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 21:46:17 2017

@author: lifenyou
"""

#!/usr/bin/env python

# encoding=utf-8

import urllib
import re
def getHtml(url):
    #page=urllib.urlopen(url)
    requst=urllib.request
    page=requst.urlopen(url)
    html=page.read().decode('utf-8')
    return html
def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

    return imglist      
   
html = getHtml("http://tieba.baidu.com/p/2460150866")
print(getImg(html)) 
