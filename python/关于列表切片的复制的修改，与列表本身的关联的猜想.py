#print("hello")

# #  创建一个用于存储外星人的空列表
# aliens = []
# #  创建 30 个绿色的外星人
# for alien_number in range (0,30):
# 	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
# 	aliens.append(new_alien)
# for alien in aliens[0:3]:
# 	if alien['color'] == 'green':
# 		alien['color'] = 'yellow'
# 		alien['speed'] = 'medium'
# 		alien['points'] = 10
# #  显示前五个外星人.
# print("这里是对切片直接修改后输出的列表")
# for alien in aliens[0:5]:
# 	print(alien)#直接修改切片，会修改原列表
# print("...")

# print("这里是对切片复制后再修改，输出的列表与复制")
# alien_copys = aliens[0:3]
# # del alien_copys[0]#删除copys内第一个后，发现原表没有受到改动，但是copys只剩两个。
# for alien_copy in alien_copys:
# 	alien_copy['color']="red"#然后再改动copys，很玄学的原表改动了2-3，第1个没有改。
# alien_copys[0]={'color': 'wihte', 'points': 5, 'speed': 'slow'}

# print("normal:")
# print(aliens[0:3])#修改切片复制版，会导致切片修改，会导致原版修改
# print("copy")
# print(alien_copys)
# print(".....")
# for alien in aliens[0:5]:
# 	print(alien)
# print(".....")

#复制切片后，修改复制，不会引起切片以及原件修改
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# # del friend_foods[0]
# friend_foods[0]=["milk"]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

#总结，其实我不确定总结的对不对，大概是在对列表的切片做copy后，对列表中是字典而言，copys与normal有关联，
#但当对copys进行了列表元素级的增删改（这里改是指重新赋值一个字典进来）时，都会断掉该元素与列表的关联。
#但是当对列表中某字典的某元素进行修改，原表也会受到修改。
#不太懂这个猜想的原理，留个印象吧。




