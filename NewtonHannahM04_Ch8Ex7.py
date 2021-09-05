Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
	file_variable = open("text.txt" , "r")
	textList = []
	for line in file_variable:
		line = line.rstrip("/n")
		mylist = line
		textList.append(mylist)
	print("finding number of uppercase Letters in text.txt file")
	totalUpCaLetters = countUpperCase(textList)
	print("number of uppercase Letters : ",totalUpCaLetters)
	print()
	print("finding number of lowercase letters in text.txt file")
	totalLoCaLetters = countLowerCase(textList)
	print("number of Lower case Letters : ",totalLoCaLetters)
	print()
	print("finding number of digits in text.txt file")
	totalDigits = countDigits(textList)
	print("number of digits : ",totalDigits)
	print()
	print("finding number of whitespaces in text.txt file")
	totalWhiteSpaces = countWhiteSpace(textList)
	print("number of whitespaces : ",totalWhiteSpaces)

	
>>> def countUpperCase(anyList):
	count = 0
	for row in range(len(anyList)):
		for i in range(len(anyList[row])):
			if anyList[row][i].isupper():
				count+= 1
	return count

>>> def countLowerCase(anyList):
	count = 0
	for row in range(len(anyList)):
		for i in range(len(anyList[row])):
			if anyList[row][i].islower():
				count+= 1
	return count

>>> def countDigits(anyList):
	count = 0
	for row in range(len(anyList)):
		for i in range(len(anyList[row])):
			if anyList[row][i].isdigit():
				count+= 1
	return count

>>> def countWhiteSpace(anyList):
	count = 0
	for row in range(len(anyList)):
		for i in range(len(anyList[row])):
			if anyList[row][i].isspace():
				count+= 1
	return count

>>> main()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    main()
  File "<pyshell#22>", line 2, in main
    file_variable = open("text.txt" , "r")
FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'
>>> 