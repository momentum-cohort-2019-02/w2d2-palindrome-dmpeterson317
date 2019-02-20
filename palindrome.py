import helper

def main():
	# assert("stunt nuts")

	userInput = input("Enter one or more sentences: ")

	text = helper.clean_text(userInput)
	
	if helper.isPalindrome(text): 
		print("is a palindrome")
	else: 
		print("is not a palindrome")


	# alternative method of evaluating boolean
	# resultVariable = helper.isPalindrome(text)
	# if resultVariable == True:
	# 	print("is a palindrome")
	# else:
	# 	print("is not a palindrome")

if __name__ == "__main__":
	main()