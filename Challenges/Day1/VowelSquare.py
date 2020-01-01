# auxiliary functions

#determine if letter is Vowel
def isVowel(char):
  if char in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
    return True
  else:
    return False

#determine if letter is top left corner of vowel square
def isVowelNext(matrix,posX,posY,nRows,nCols):
  nextX = posX+1
  nextY = posY+1
  if nextX < nCols and nextY < nRows:
    vowelX = matrix[posY][nextX]
    vowelY = matrix[nextY][posX]
    vowelCorner = matrix[nextY][nextX]
    if isVowel(vowelX) and isVowel(vowelY) and isVowel(vowelCorner):
      return True
    else:
      return False
  else:
    return False

#code goes here
def VowelSquare(strArr):
  pos = "not found"
  nRows = len(strArr)
  nCols = len(strArr[0]) if  nRows > 0 else 0 
  for i, row in enumerate(strArr):
    for j, letter in enumerate(row):
      if isVowel(letter):
        if isVowelNext(strArr,j,i,nRows,nCols):
          if(pos != "not found"):
            pos = pos
          else:
            pos = str(i)+'-'+str(j)

  return pos

# keep this function call here 
print(VowelSquare(input()))