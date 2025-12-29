# Reverse string

text = str(input("Enter a text: "))

def reverse_string(text):
    rev_text = []
    for i in range(len(text)-1,-1,-1):
        rev_text.append(text[i])
    return ''.join(rev_text)

result = reverse_string(text)
print(result)