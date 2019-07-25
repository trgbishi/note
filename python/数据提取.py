#command:python ***.py  filename  "keyword"
#!/usr/bin/env python
#-*- coding: utf-8 -*-
#filename: readLogfile.py

import matplotlib.pyplot as plt
import re
import sys
import numpy

# Open logfile
input = open(str(sys.argv[1]), 'r')
point_x = []
point_y = []
fig = plt.figure()
ax = fig.add_subplot(111)  
# Get the start time of log file
for line in input:  
    time = re.search('[-+]?[0-9]*\.?[0-9]+', line)
    if time:
        time_start = float(time.group())
        break



# Iterate key words
for j in range(2, len(sys.argv)):
    key_word_list = []
    key_word = sys.argv[j]
    print key_word
    
    # Extract key word in each line
    for line in input:
        match_key_word_in_line = re.search(key_word,line)
        if match_key_word_in_line:
            rs_key_word = re.findall('[-+]?[0-9]*\.?[0-9]+', line)
            if rs_key_word:
#		print rs_key_word
                data = []
		data_for_mat = []
                for i in range(2, len(rs_key_word)):
                    data.append(float(rs_key_word[i])) 

                #if (len(data) > 1):
		point_x.append(rs_key_word[1])
		point_y.append(rs_key_word[2])
		data_for_mat.append(rs_key_word[1])
		data_for_mat.append(rs_key_word[2])
		#c.putpixel([point_x,point_y],(5,5,5))
                key_word_list.append(data_for_mat)
		    
#产生x,y坐标
    if (len(key_word_list)):
        # Save data to .txt file
        file_object = open(key_word + '.txt','w')
        file_object.truncate()
        for key_word_line in key_word_list:
            for c in key_word_line:
                file_object.write(str(c))
                file_object.write("   ")
            file_object.write("\n")
        file_object.close()

#ax.scatter(point_x,point_y,c="y")  
#plt.show()

point_x = map(float,point_x)
point_y = map(float,point_y)