#!/usr/bin/python
# -*- coding: UTF-8 -*-

# HTTP 头部
print "Content-Disposition: attachment; filename=\"res.txt\"";
print
# 打开文件
fo = open("res.txt", "rb")

str = fo.read();
print str

# 关闭文件
fo.close()
