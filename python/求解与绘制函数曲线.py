#求解函数
#point_x,point_y为x坐标集合，y坐标集合，9为最高次数
f1 = numpy.polyfit(point_x,point_y, 9)  
p1 = numpy.poly1d(f1)  
print(p1)  


#绘图代码
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,50,1)
y=0.1052*x**3 - 7.685*x**2 + 126.9*x + 464.5
plt.plot(x,y)
plt.show()