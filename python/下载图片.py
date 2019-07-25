#以图虫网为样本

import requests
import re
from PIL import Image
from io import BytesIO

input = open('photoUrl.txt')#网址链接，源代码数据中有图片的地址

for line in input:
    web_url = requests.get(r''+line)
    photo_url = re.findall('multi-photo-image" src="(.*?)" alt="">',web_url.text)#正则锁定图片地址
    for photo in photo_url:#遍历每一张图片，依次写入
        photo_name = re.findall('/f/(.*?).jpg',photo) #不加文件类型后缀的图片名
        image = Image.open(BytesIO(requests.get(photo).content))
        image.save(photo_name[0]+'.jpg')
