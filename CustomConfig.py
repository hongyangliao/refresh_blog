# -*- coding: utf-8 -*-
# 和arts一起组成博客地址
url = 'https://blog.csdn.net/blue5945/article/details/'

# 代理地址
proxys = [{'http': '101.71.232.229'}, {'http': '47.93.3.242'}, {'http': '115.218.217.92'},
          {'http': '117.87.178.188'}, {'http': '115.218.127.67'}, {'http': '114.235.22.159'}]

# 和url一起组成博客地址
arts = ['79811022','79273835','79203230','79203253','79203203','79203178',
       '79202941','79202793','79202772','79202742','79202716','79202675','79202629','79202554']

# 伪造浏览器的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip',
    'Connection': 'close',
    # 防止防盗链
    'Referer': 'https://blog.csdn.net/'
    }