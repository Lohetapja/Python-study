# Palindrome

text = str(input("Enter a sentence: ")) 
text = text.lower().replace(" ", "") 

def palindrome(text):
    if text == text [::-1]:
        return True
    else:
        return False

resualt = palindrome(text)
if resualt == True:
    print("It is a palindrome")
else:
    print("It is not a palindrome")