#code goes here:
def encrypt(word):
    newWord = ''
    sufix = 'aca'
    word = word[::-1] #reverse the input
    for s in word:
        if(s == 'a'):
            newWord+='0'
        elif(s == 'e'):
            newWord+='1'
        elif(s == 'o'):
            newWord+='2'
        elif(s == 'u'):
            newWord+='3'
        else:
            newWord+=s
    return newWord+sufix

print(encrypt(input()))
