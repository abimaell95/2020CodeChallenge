import math
#code goes here
def isPrime(num):
	if(num <= 1):
		return False
	bot = int(math.sqrt(num))
	for i in range(bot):
		d = i+1
		if d >= 2 :
			if num % d == 0 :
				return False
	return True
			

def primeNumbers(num):
	countPrime = 0
	for i in range(num):
		n = i+1
		if isPrime(n):
			countPrime+=1
	return countPrime

print(primeNumbers(int(input())))