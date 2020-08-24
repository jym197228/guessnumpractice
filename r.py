import random
r = random.randint(1, 100)
while True:
	num = input('請猜猜數字: ')
	num = int(num)
	if num == r:
		print('您猜中了!')
		break
	elif num > r:
		print('答案比您輸入的還要小')
	else:
		print('答案比您輸入的還要大')