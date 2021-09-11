import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	gue = input('請輸入數字')
	gue = int(gue)
	if gue == r:
		print('終於猜對了')
		print('這是你猜的第',count,'次')
		break
	elif gue >= r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第',count,'次')