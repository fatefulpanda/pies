def fibo():
	x = int(input("How many Fibonnaci numbers do you want?: "))
	i = 1
	if x == 0:
		fib = []
	elif x == 1:
		fib =[1]
	elif x == 2:
		fib = [1,1]
	elif x > 2:
		fib = [1,1]
		while i < (x - 1):
			fib.append(fib[i]+fib[i-1])
			i+=1
	return fib
print(fibo())
input()
