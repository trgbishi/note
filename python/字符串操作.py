title_content = re.findall('<title>(.*?)</title>', title.text) #获取<title> 与 </title>之间的字符串

if title_content[0].find("_科技_") != -1  #在title_content[0]里寻找 关键字，没有返回-1，有的话返回位置索引
