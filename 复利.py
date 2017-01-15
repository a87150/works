def power():
	s = float(input('请输入数字：'))
	x = float(input('请输入增长倍数：'))
	n = int(input('请输入次数：'))
	while n > 0:
		n = n - 1
		s = s * x
	print(s)

power()