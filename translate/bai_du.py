#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    author='BilibiliRiven',
    author_email='BilibiliRiven@gmail.com'or'958403316@qq.com'
    fuction:
    Day:%s
"""
# 百度翻译页面翻译发送机制并不是通过post，发送要翻译的内容，而是通过在【http://fanyi.baidu.com/#en/zh/】之后附加翻译内容
"""
翻译举例子翻译”hello world“
http://fanyi.baidu.com/#en/zh/hello%20world
可见百度翻译的通信机制是把要翻译的内容变成url编码的格式附加在页面url之后。
"""
import urllib.request, urllib.parse
import json

class BaiDu(object):
    def __init__(self):
        pass
    def send(self, str):
        url = 'http://fanyi.baidu.com/v2transapi'
        data = {"from": 'en', 'to': 'zh', 'query': str, 'transtype': 'realtime',
                'simple_means_flag': 3}
        url = 'http://fanyi.baidu.com/v2transapi'
        data = urllib.parse.urlencode(data).encode('utf-8')
        head={}
        head ['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        req = urllib.request.Request(url, data, head)
        content = urllib.request.urlopen(req)
        content = content.read().decode('utf-8')
        content = json.loads(content)
        return content['trans_result']['data'][0]['dst']

