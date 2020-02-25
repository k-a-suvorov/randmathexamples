#Конструкция для обработки всяких ошибок]

try:
	switch = True #
	import random # библиотека генерации случайного числа

	#Ввод двуч чисел
	x = int(input('x = '))
	y = int(input('x = '))
	z = 0


	#проверка условия - если условия не верны - выход из программы
	if ((x > y) or (x == y) or (x < 5) or (y < 5)):

		print(F'Неверно условие Должно быть {x} < {y}')
		switch = False

	#Если условие верно
	elif (x < y):

		a = random.randint(x, y) # Генерация числа

	#Если число кратно 5
		if (a % 5 == 0):
			print(f'Число {a} кратно 5')
	#Если число не кратно 5 выводим 0
		else:
			print(f'Число {a} не кратно 5. Вот вам {z}')	

except ZeroDivisionError:
    print('On zero share cannot be!')		
except ValueError:
    print("You have some mistake of userinput Value!")
except TypeError:
   print("You have some mistake of type Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )
except ArithmeticError:
	print("Arithmetic operations was broken!")
except ImportError:
	print("Some modules not loaded, please check your source code!")
except IOError:
	print('An error IO file!')		
