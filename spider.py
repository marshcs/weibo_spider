# -*- coding: utf-8 -*-

'''
准备：
1、安装 chrome 插件小乐图客 https://chrome.google.com/webstore/detail/zzllrr-imager-geek/gfjhimhkjmipphnaminnnnjpnlneeplk

开始：
1、使用 www.weibo.com 的搜索功能，搜索 #猫# ，切换到图片选项，此时可以看见一张张猫的图片的缩略图, 下拉搜索结果，直到数量足够，500张。
2、单击插件图标，'添加任务'，'获取网址'，将所有的网址复制到'cat.txt'
3、将代码中的 key 变量改为所需要的类型名。
4、运行代码
'''

import urllib
import os
import shutil,time,random


"""
# 保存单一帖子中所有的图片，从1开始编号
# args:
        all_pic_urls  list    单一帖子所有图片链接
        folder_name   string  存储文件夹名（帖子名）    
"""    
def download_image(all_pic_urls,folder_name):
    n = 0
    for pic_url in all_pic_urls:
        if n % 20 == 0:
            sleeptime=random.randint(0,30) / 20
            time.sleep(sleeptime)
        n+=1
        file_name= str(n)+'.jpg'
        urllib.request.urlretrieve(pic_url,folder_name+'\\'+file_name)

key = 'cat'
folder_name = '.\\pic\\{}'.format(key)
if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
os.mkdir(folder_name)    
txt_new = []
with open('{}.txt'.format(key),'r') as f:
    text = f.readlines()
    for txt in text:
        if txt.startswith(r'https://wx'):
            txt_new.append(txt.replace("thumb180","mw600"))

download_image(txt_new,folder_name)