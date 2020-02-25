import random # библиотека генерации случайного числа
	#Ввод двуч чисел
try:

	x = int(input('x = '))
	y = int(input('x = '))

	a = random.randint(x,y)
	z = 0

	if ((x > y) or (x == y)):
		print('Не верное введены значения')

			
	if (a % 5 == 0):
		print('!!!')
	else:
		print(z)	

	print(a)

except Exception:
	print(f'Это что ещё такое? {y} не должен быть 0')
