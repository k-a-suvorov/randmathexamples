import random # библиотека генерации случайного числа
	#Ввод двуч чисел
x = int(input('x = '))
y = int(input('x = '))

a = random.randint(x,y)
z = 0

if (a % 5 == 0):
	print('Ура: ', a)
else:
	print('Не ураюю (((', z)	

print(a)	
