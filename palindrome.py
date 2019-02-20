import helper

def main():

	userInput = input("Enter one or more sentences: ")

	text = helper.clean_text(userInput)
	if helper.isPalindrome(text): 
		print("is a palindrome")
	else:
		print("is not a palindrome")

if __name__ == "__main__":
	main()