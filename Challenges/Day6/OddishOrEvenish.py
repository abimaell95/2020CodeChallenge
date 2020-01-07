#code goes here:
def oddish_or_evenish(num):
    sumDigit = 0
    for digit in num:
        sumDigit += int(digit)
    return "Evenish" if sumDigit%2 == 0 else "Oddish"

print(oddish_or_evenish(input()))
