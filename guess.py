import random

r = random.randint(1, 100)

while True:
	gue = input('請輸入數字')
	gue = int(gue)
	if gue == r:
		print('終於猜對了')
		break
	elif gue >= r:
		print('比答案大')
	else:
		print('比答案小')