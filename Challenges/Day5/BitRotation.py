#code goes here:
def bit_rotate(n,m,d):
    newBin = ''
    nBin = "{0:b}".format(n)
    rotation = -1 if d else 1
    if m > len(nBin):
        prop = m%len(nBin)
        if(prop == 0):
            return int(nBin,2)
        else:
            m = prop
    n = m*rotation
    print(n)
    for i in range(len(nBin)):
        if n < len(nBin):
            s = nBin[n]
            newBin += s 
        else:
            n = 0
            s = nBin[n]
            newBin += s
        n = n + 1
    print(newBin)
    return int(newBin,2)

n = int(input())
m = int(input())
dInput = input()
d = True if dInput == 'True' else False
print(bit_rotate(n,m,d))