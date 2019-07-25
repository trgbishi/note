# -*- coding: utf-8
import os
count = 0
nowDir = ""
fileName = []

#读取文件
def readFile(filepath):
    f1 = open(filepath, "r")
    global nowDir
    nowDir = os.path.split(filepath)[0]             #获取路径中的父文件夹路径
    fileName.append(os.path.split(filepath)[1])           #获取路径中文件名
    
    global count
    count+=1

#遍历所有文件
def eachFile(filepath):
    pathDir = os.listdir(filepath)      #获取当前路径下的文件名，返回List
    for s in pathDir:
        newDir=os.path.join(filepath,s)     #将文件名加入到当前文件路径后面
        if os.path.isfile(newDir) :         #如果是文件
            if os.path.splitext(newDir)[1]==".py":  #判断是否是py
                readFile(newDir)                     #读文件
                pass
        else:
            eachFile(newDir)                #如果不是文件，递归这个文件夹的路径
            
filepath = os.getcwd() + "/"
eachFile(filepath)

for tmp_name in fileName:
    print tmp_name
print "end"
print "共处理"+bytes(count)+"个txt"