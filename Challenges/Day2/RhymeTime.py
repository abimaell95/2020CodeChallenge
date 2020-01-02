#auxiliary function

#letter is vowel
def isVowel(char):
	if char in ('A','a','E','e','I','i','O','o','U','u'):
		return True
	else:
		return False

def stripNotVowel(word):
	stripedWord = ''
	for letter in word:
		if isVowel(letter):
			stripedWord += letter
	return stripedWord

#code goes here
def doesRhyme(sentence1,sentence2):
	lastVowels1 = stripNotVowel(sentence1.split(' ')[-1])
	lastVowels2 = stripNotVowel(sentence2.split(' ')[-1])
	return True if lastVowels1.lower() == lastVowels2.lower() else False


sentence1 = input()
sentence2 = input()

print(doesRhyme(sentence1,sentence2))