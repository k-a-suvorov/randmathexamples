try:
	import random

	x = int(input('x = '))
	y = int(input('y = '))

	a = random.randint(x,y)

	def zeroPrint():
		global a
		z = 0
		print(f'Zero {a}', z)
	
	if ((x > y) or (x == y)):
		print('Не верное введены значения')
	elif (y > x):
			
		if (a % 5 == 0):
			print('!!!')
		elif (a % 5 != 0):
			print (a)
			zeroPrint()

	print(a)

except Exception:
	if (y == 0):
		print(f'Это что ещё такое? {y} не должен быть 0')
	else:
		zeroPrint()
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
