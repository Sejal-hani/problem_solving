# enter the number
n=input().strip()

# enter the digfit
digit = input().strip()

def count_digit(n, digit):

	count = 0
	for d in n:
		if d == digit:
			count += 1	

	return count


print(count_digit(n, digit))


	



