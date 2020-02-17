#usr/bin/python3
#Simple calc
import os
import random
import inputdef as id
import mathdefs as md

#print('This is simle calc')
try:

	#Initialize
	
	playGame = True
	count = 0
	right = 0
	score = 0

	z1 = ""

	#Processing

	while playGame:
		print ("*" * 120, "\n")
		print(f'Your score: {score}')
		print(f'Your Task: {count}')
		print(f'Your right answers: {right}')
		print ("*" * 120, "\n")
		
	#Initialize
		lowDigit = 1
		highDigit = 100
		x = random.randint(lowDigit, highDigit)
		y = random.randint(lowDigit, highDigit)
		sign = random.randint(0, 3)


		if (sign == 0):
			#znak = '+'
			z = x + y
			print(f'{x} + {y} = ? ')
			#print(z)
			os.system('python mathdefs.py')
			
			z1 = id.inputResult (z1)
			if (z == z1):
				count += 1
				right += 1
				score += 5
		
				print(F'Your answer is right! {z} = {z1}!')
				print ("*" * 120, "\n")
			else:
				count += 1
				score -= 5	
				print(F'You got a mistake! the result is: {z}')
				print ("*" * 120, "\n")
		elif (sign == 1):
			#znak = '-'
			z = x - y
			print(f'{x} - {y} = ? ')
			#print(z)
			os.system('python mathdefs.py')
			
			z1 = id.inputResult (z1)
			if (z == z1):
				count += 1
				right += 1
				score += 5
		
				print(F'Your answer is right! {z} = {z1}!')
				print ("*" * 120, "\n")
			else:
				count += 1
				score -= 5
		
				print(F'You got a mistake! the result is: {z}')
				print ("*" * 120, "\n")
		elif (sign == 2):
			#znak = '*'
			z = x * y
			print(f'{x} * {y} = ? ')
			#print(z)
			os.system('python mathdefs.py')
			
			z1 = id.inputResult (z1)
			if (z == z1):
				count += 1
				right += 1
				score += 5
		
				print(F'Your answer is right! {z} = {z1}!')
				print ("*" * 120, "\n")
			else:
				count += 1
				score -= 5
		
				print(F'You got a mistake! the result is: {z}')
				print ("*" * 120, "\n")
		elif (sign == 3):
			#znak = '/'
			z = x // y
			print(f'{x} / {y} = ? ')
			#print(z)
			os.system('python mathdefs.py')
			if (y == 0):
				playgame = False
			else:
				z1 = id.inputResult (z1)
		
				print(f'{x} / {y} integer part of the branch number = ? ')
				print ("*" * 120, "\n")
				if (z == z1):
					count += 1
					right += 1
					score += 5
		
					print(F'Your answer is right! {z} = {z1}!')
					print ("*" * 120, "\n")
				else:
					count += 1
					score -= 5	
		
					print(F'You got a mistake! the result is: {z}')
					print ("*" * 120, "\n")
	
		
		print("Type stop to Exit")
		print ("*" * 120, "\n")
		
		
except ZeroDivisionError:
    print('On zero share cannot be!')		
except ValueError:
    print("You have some mistake of userinput Value")
except TypeError:
   print("You have some mistake of type Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!" )
