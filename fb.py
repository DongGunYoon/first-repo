def do_fizzbuzz(num):
	answer = ['FIZZBUZZ' if i%15==0 else 'FIZZ' if i%3==0 else "BUZZ" if i%5==0 else i for i in range(1, num+1)]
	print(answer)

if __name__=='__main__':
	do_fizzbuzz(int(input()))