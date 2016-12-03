#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    author='BilibiliRiven',
    author_email='BilibiliRiven@gmail.com'or'958403316@qq.com'
    fuction:
    Day:%s
"""
import json
import urllib.parse
import urllib.request


class You_Dao(object):
    def __init__(self):
        pass

    def send(self, str):
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link"
        """
        type:AUTO
        i:I love MOOk
        doctype:json
        xmlVersion:1.8
        keyfrom:fanyi.web
        ue:UTF-8
        action:FY_BY_ENTER
        typoResult:true
        """
        data = {}
        data['type'] = 'AUTO'
        data['i'] = str
        data['doctype'] = 'json'
        data['xmlVersion'] = "1.8"
        data['keyfrom'] = "fanyi.web"
        data['ue'] = "UTF-8"
        data = urllib.parse.urlencode(data).encode('utf-8')
        head={}
        head ['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
        req = urllib.request.Request(url, data, head)

        content = urllib.request.urlopen(req)

        content = content.read().decode('utf-8')
        content = json.loads(content)

        return content['translateResult'][0][0]['tgt']