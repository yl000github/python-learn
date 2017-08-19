#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import threading
from multiprocessing import Pool, cpu_count
import requests
from bs4 import BeautifulSoup
headers = {'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
'Referer':'http://www.mmjpg.com/mm/1/2'




}
dir_path = r"F:\mmjpg"      # 下载图片保存路径


def save_pic(pic_src):
    """ 将图片下载到本地文件夹 """
    try:		
        print("download path: {}".format(pic_src))
        img = requests.get(pic_src, headers=headers, timeout=10)
        imgname = "f:/pic_cnt_{}.jpg".format( 1)
        # with open(imgname, 'ab') as f:
        with open(imgname, '2') as f:
            f.write(img.content)
            print(imgname)
    except Exception as e:
        print(e)
		
save_pic("http://img.mmjpg.com/2015/70/1.jpg")