option = int(input("Do you want to \n 1)Encrypt\n 2)Decrypt: \n"))


def vigenere(text, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final = ''
    for char in text:
        key_index = 0
        key_char = key[key_index % len(key)]
        offset = alphabet.find(key_char)
        new_index = (offset * direction + alphabet.find(char)) % 26
        final += alphabet[new_index]
    return final


if option == 1:
    message = str(input("Enter Your message: "))
    secret = str(input("Enter Your Secret Key: "))
    print(f"Encrypted Message is : {vigenere(message,secret)}")
else:
    message = str(input("Enter Your Encrypted message: "))
    secret = str(input("Enter Your Secret Key: "))
    print(f"Decrypted Message is : {vigenere(message, secret, -1)}")
