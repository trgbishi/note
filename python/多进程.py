#直接贴demo吧
#遍历b站前1w个视频，并输出标题信息
from multiprocessing import Pool
from time import sleep
import requests
import re

def getTitle(x):
    for i in range(100):
        title = requests.get(r'https://www.bilibili.com/video/av'+str(x*100+i))
        print(re.findall('<title>(.*?)_', title.text))

def main():
    pool = Pool(processes=100)   #max
    for i in range(1,101):
        result = pool.apply_async(getTitle, (i,))
    pool.close()
    pool.join()
    if result.successful():
        print("successful")
        
if __name__ == "__main__":
    main()
