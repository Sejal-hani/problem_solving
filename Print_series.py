nums  = input().strip()
m = 0
sums = 0

for i in range(1,len(nums)+1):

	n = int(nums[-i])
	# digit = n%10
	sums += n * (2**m)
	m = m + 1

print(sums)

