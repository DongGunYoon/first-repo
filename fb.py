def do_fizzbuzz(num):
	for i in range(1, num+1):
		if i%15==0:
			print("FIZZBUZZ")
		elif i%3==0:
			print("FIZZ")
		elif i%5==0:
			print("BUZZ")
		else:
			print(i)

if __name__=='__main__':
	do_fizzbuzz(int(input()))