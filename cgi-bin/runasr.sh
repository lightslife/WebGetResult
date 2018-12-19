#!/bin/bash
 
 
echo "Content-Type:text/html; Charset=utf-8"
echo ""
 
echo "<br/>"
echo "<br/>"
echo "<br/>"
echo "<center><h2>1.程序正在执行，在执行成功之前请勿关闭该窗口</h2></center>"

if [[ "$REQUEST_METHOD" == "POST" ]];then

 cd meeting-asr-spkd/
 bash run.sh >> foo.log
 cd ..
 
 echo "<br/>"
 echo "<center><h2>2.程序执行成功，返回上一页下载查看程序执行结果.</h2></center>"

fi
