# import re

def isPalindrome(text):
	i = 0
	isPal = True

	while isPal == True and i < len(text):
		if text[i] != text[-1 - i]:
			return False
		i += 1
		return True

def clean_text(text):
    """
    Given a text, return the text with no spaces or punctuation and all lowercased.
    """
    new_text = ""
    text = text.lower()
    for character in text:
        if character.isalpha():
            new_text = new_text + character
    return new_text