import random
start = input('請輸入隨機整數範圍開始值: ')
end = input('請輸入隨機整數範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜猜數字: ')
	num = int(num)
	if num == r:
		print('您猜中了!')
		print('您總共猜了', count, '次')
		break
	elif num > r:
		print('答案比您輸入的還要小')
	else:
		print('答案比您輸入的還要大')
	print('您猜了', count, '次')