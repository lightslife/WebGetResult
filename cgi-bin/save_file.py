#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# 获取文件名
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
   # 设置文件路径 
   fn = os.path.basename(fileitem.filename.replace("\\","/"))
   open(fn, 'wb').write(fileitem.file.read())

   message = '文件 "' + fn + '" 上传成功，请返回上一页执行程序。'
   
else:
   message = '文件没有上传'
   
print """\
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8">
<title>上传语音文件</title>
</head>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,)
