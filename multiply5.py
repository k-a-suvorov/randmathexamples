#Конструкция для обработки всяких ошибок]

try:
	import random # библиотека случвйных значений

	#Ввод значений
	x = int(input('x = '))
	y = int(input('y = '))
	
	#Проверка условий ввода	
	if ((x > y) or (x == y)):
		print('Не верное введены значения')
	else:	
		#Генерация случайного числа
		a = random.randint(x,y)

	#Функция вывода 0
	def zeroPrint():
		global a
		z = 0
		print(F'Zero {z} ', end='')
	
	
	if (y > x):
		
		#вывод кратного числа 		
		if (a % 5 == 0):
			print('!!!')
		elif (a % 5 != 0):
			#Если не кратно - 0
			print (a)
			zeroPrint()
	
	print(a)
	
	#Вывод всех чисел кратных 5
	for i in range(x, y, 1):
		if (i % 5 == 0):
			print(" ", i, end="")
		elif (i % 5 != 0):
			zeroPrint()	

#Если y равен 0
except Exception: 
	if (y == 0):
		print(f'Это что ещё такое? {y} не должен быть 0')
	else:
		zeroPrint()
# Обработка ошибок вводимых значений		
except ValueError:
    print("Некоректны вводимые значения")
#Обработка типов переменных
except TypeError:
   print("Некоректный тип данных")
#Обработка системных ошибок
except SystemError:
	print("Обычная системная ошибка" )
# Обработка ошибок загрузки модулей
except ImportError:
	print("Нужные модули не загружены")

