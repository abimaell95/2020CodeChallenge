#code goes here
def carryDigits(integer1, integer2):
	countCarry = 0
	carry = 0
	greatNum = integer1 if integer1 > integer2 else integer2
	while(greatNum != 0):
		i = integer1%10
		j = integer2%10
		sum = i+j+carry
		if(sum > 9):
			carry = sum-9
			countCarry+=1
		else:
			carry = 0
		integer1 = integer1 // 10
		integer2 = integer2 // 10
		greatNum = greatNum // 10
	return countCarry


n1 = int(input())
n2 = int(input())

print(carryDigits(n1,n2))