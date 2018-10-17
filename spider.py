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

from urllib import request
import requests
import os
import shutil,time,random


"""
# 保存单一帖子中所有的图片，从1开始编号
# args:
        all_pic_urls  list    单一帖子所有图片链接
        folder_name   string  存储文件夹名（帖子名）    
"""    
def download_image(all_pic_urls,folder_name,start=0,end = None):
    n = start
    for pic_url in all_pic_urls:
        if n % 20 == 0:
            sleeptime=random.randint(0,30) / 20
            time.sleep(sleeptime)
            print('{:d} image downloaded'.format(n))
        n+=1
        file_name= str(n)+'.jpg'
        request.urlretrieve(pic_url,folder_name+'/'+file_name)
        
def download_image_req(all_pic_urls,folder_name, pic_size = 'large', start=0, end=None):
    n = start
    for pic_url in all_pic_urls:
        n+=1
        file_name= str(n)+'.jpg'
        full_file_name = folder_name + './' + file_name
        if os.path.isfile(full_file_name):
            print('{}.jpg exists'.format(n))
        else:
            if n % 20 == 0:
                sleeptime=random.randint(0,30) / 20
                time.sleep(sleeptime)
            r=requests.get(pic_url,stream = True, timeout = 3)
            if r.status_code == 200:
                print('{:d} image downloaded'.format(n))
                with open(full_file_name, 'wb') as f:
                    for chunk in r.iter_content(256):
                        f.write(chunk)

def create_folder(folder_name_list):
    for folder_name in folder_name_list:
        if not os.path.exists('./{}'.format(folder_name)):
            os.mkdir('./{}'.format(folder_name))


# 需要修改的部分
key = 'sky'
new_filename = 'sky2'
# 下载图片的尺寸   large:原图   mw600:中图   thumb180: 缩略图
pic_size = "mw600"
#

folder_name     = './pic/{}'.format(key)
lib_file_name   = './lib/{}.txt'.format(key)
create_folder(['pic','lib','new',folder_name])

with open('./new/'+new_filename+'.txt','r') as f, open(lib_file_name,'a+') as f_lib:
    new_url_list = f.readlines()
    f_lib.seek(0)
    lib_list = f_lib.readlines()
    url_new = []
    for url in new_url_list:
        if url.startswith(r'https://wx') & (url not in lib_list):
#            txt_new.append(txt.replace("thumb180",pic_size))
            url_new.append(url)
lib_list.extend(url_new)
with open(lib_file_name,'a') as f_lib:
    f_lib.writelines(url_new)

dwn_lib_list = [url.replace("thumb180",pic_size) for url in lib_list]
input('total number of picture is {:d}, press any key to start downloading, or Ctrl+C to stop'.format(len(lib_list)))
download_image_req(dwn_lib_list,folder_name,pic_size = pic_size)