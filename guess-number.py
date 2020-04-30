# 產生一個隨機整數1到100 不要印出
# 讓使用者重複輸入去猜
# 猜對的話 印出“猜對了！”
# 猜錯的話 要印出“比答案大或小”
# 追加功能1：印出猜了幾次

import random

r = random.randint(1,100)
count = 0 # 追加功能1
while True:
	count += 1 # count = count + 1 # 追加功能1
	num = input('請猜數字:') # input字串
	num = int(num) # 轉換回整數
	if num == r:
		print('猜對了！')
		print('這是你猜的第', count, '次') # 追加功能1
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次') # 追加功能1
