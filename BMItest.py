def BMItest():
	height = float(input('请输入身高m：'))
	weight = float(input('请输入体重kg：'))
	bmi=(weight/(height*height))
	if bmi<=18.5:
		print('轻')
	elif bmi<=24:
		print('正常')
	elif bmi<=29:
		print('过重')
	elif bmi<=34:
		print('肥胖')
	else:
		print('严重肥胖')
	print('bmi = %f'%bmi)
	
BMItest()