# -*- coding: utf-8
#注意:会将输入的根目录以及其下所有文件夹和文件名全部替换

import os

old_str = "old"
new_str = "new"


#遍历所有文件
def eachFile(filepath):
    pathDir = os.listdir(filepath)      #获取当前路径下的文件名，返回List
    for s in pathDir:
        newDir=os.path.join(filepath,s)     #将文件名加入到当前文件路径后面
        if os.path.isfile(newDir) :         #如果是文件
            if old_str in newDir:  #判断是否包含
                newnew = newDir.replace(old_str,new_str)
                os.renames(newDir,newnew) 
                pass
        else:
            eachFile(newDir)                #如果不是文件，递归这个文件夹的路径
            print(newDir)
            
###根目录
filepath = 'E:\\test'
eachFile(filepath)
