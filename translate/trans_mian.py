#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    author='BilibiliRiven',
    author_email='BilibiliRiven@gmail.com'or'958403316@qq.com'
    fuction:
    Day:%s
"""
import bai_du
import you_dao

class Translater(object):
    def __init__(self, a):  # 参数传入1，用百度翻译，否则用有道翻译。
        if a == 1:
            self.sendor = bai_du.BaiDu()
        else:
            self.sendor = you_dao.You_Dao()

tras = Translater(1)  # 此时用百度翻译
print(tras.sendor.send("Hello World"))
