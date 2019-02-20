import helper

def main():

	userInput = input("Enter one or more sentences: ")
	# breakpoint()
	text = helper.clean_text(userInput)
	if helper.isPalindrome(text): 
		print("Y")
	else:
		print("N")

if __name__ == "__main__":
	main()