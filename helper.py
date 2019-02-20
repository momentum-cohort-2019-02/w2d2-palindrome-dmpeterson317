# import re

def isPalindrome(text):
    i = 0	
        
    while i < len(text) // 2:
        # print(text, text[i], text[-1 - i])
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