# -*- coding: utf-8 -*-

import requests

pic_url = 'https://wx2.sinaimg.cn/thumb180/007lLjqyly1fw4440whiwj31hc0u0dnh.jpg'
r=requests.get(pic_url)
with open('pic.jpg','w') as f:
    f.write(r.content)