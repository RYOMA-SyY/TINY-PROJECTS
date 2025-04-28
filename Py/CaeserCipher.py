# Encryption
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
textEncry = str(input("Enter Your Text: ").lower())

 
textEN = []
shift = 6

for char in textEncry:
    if char in alphabets:
        index = alphabets.index(char)
        new_index = (index + shift) % 26
        textEN.append(alphabets[new_index])
    else:
        textEN.append(char)

encrypted_text = ''.join(textEN)
print("Encrypted Text:", encrypted_text)