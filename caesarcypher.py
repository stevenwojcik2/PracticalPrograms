def caesarcipher():
	message = input("Enter your secret message: ")
	shift = int(input("Shift amount: "))

	for character in message:
		#Uppercase letters
		if ord(character) >= 65 and ord(character) <= 90:
			code = ((ord(character)-65+shift)%26)+65
			crypt = chr(code)
			print(crypt, end="")
		#Lowercase letters
		elif ord(character) >= 97 and ord(character) <= 122:
			code = ((ord(character)-97+shift)%26)+97
			crypt = chr(code)
			print(crypt, end="")
		#for special characters
		else:
			print(character)
	print("")

caesarcipher()