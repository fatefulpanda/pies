#menu message
menu = ('\n0 - enter a number\n' + '1 - display current number\n' +
	'2 - divisibility checking\n' + '3 - perfect checking\n' +
	'4 - triangular checking\n' + '5 - quit')

user_num = None
user_choice = '-1'
#ask user for input until 5 is entered
while user_choice != '5':	
	#ask for input
	print(menu)
	user_choice = input('Please make a choice:')
	
	#option 0: enter a number
	if user_choice == '0':
		user_num = int(input('What is your number? '))
		while user_num <= 0:
			user_num = int(input('Must be positive, please! ' +
				'What is your number? What is your number? '))

	#option 1: display current number	
	elif user_choice == '1':
		#check if number has been entered
		if user_num == None:
			print('No number yet - please input a number and try again.')
		else:
			print('The current number is ' + str(user_num) + '.')
	
	#option 2: divisibility checking
	elif user_choice == '2':
		#check if number has been entered
		if user_num == None:
			print('No number yet - please input a number and try again.')
		else:
			num_length = len(str(user_num))
			sum = 0
			for i in range(num_length):
				sum = sum + int(str(user_num)[i])
			if sum%3 == 0:
				print(str(user_num) + ': is a multiple of 3')
			else:
				print(str(user_num) + ': is not a multiple of 3')	
		
	#option 3: perfect checking
	elif user_choice == '3':
		#check if number has been entered
		if user_num == None:
			print('No number yet - please input a number and try again.')
		else:
			sum = 0
			for i in range(1, int((user_num/2)+1)):
				if user_num%i == 0:
					sum = sum + i
			if sum > user_num:
				print(str(user_num) + ': is a abundant number')
			elif sum < user_num:
				print(str(user_num) + ': is a deficient number')
			else:
				print(str(user_num) + ': is a perfect number')
	
	#option 4: triangular checking
	elif user_choice == '4':
		#check if number has been entered
		if user_num == None:
			print('No number yet - please input a number and try again.')
		else:
			sum = 0
			tri_num=0
			while sum < user_num:
				tri_num = tri_num + 1
				sum = sum + tri_num
			print(str(user_num) + ': covered by triangular number #' + 
				str(tri_num))

	#option 5: quit
	elif user_choice == '5':
		print('Goodbye!')
	
	#invalid input
	else:
		print("I didn't understand, please try again.")
	