2d图像
x=2162
y=2162
c = Image.new("RGB",(x,y),(255,255,255))
f = open("/home/yaobc/py_test/testfile.txt")             # 读取数据，返回一个文件对象 
line = f.readline()             # 读行，读下一行只要再写一遍
ranges_temp = re.split(',',line) #按 ','分词
ranges = map(float,ranges_temp) #字符串list转化为float list
c.putpixel([point_x+k,point_y+l],(color,color,color)) #画图

3d图像
fig = plt.figure()
ax = Axes3D(fig)
plt.xlabel('x')  #坐标轴标签
ax.scatter(point_x,point_y, Z,c="y")  #绘图
plt.show() #show