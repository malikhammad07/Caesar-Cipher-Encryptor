print("===================================")
print("     Caesar Cipher Encryptor")
print("===================================")

text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift key (1-25): "))

# If user enters a number greater than 26
shift = shift % 26

print("===================================")
print("Original Text :", text)
print("Shift Key     :", shift)


# ------------------ Encryption Function ------------------

def caesar_cipher_encrypt(text, shift):

    encrypted_text = ""

    for char in text:

        if char.isalpha():

            # Check uppercase or lowercase
            if char.isupper():
                shift_base = ord("A")
            else:
                shift_base = ord("a")

            # Convert letter to position (0-25)
            position = ord(char) - shift_base

            # Shift the position
            position = position + shift

            # Keep position between 0 and 25
            position = position % 26

            # Convert back to ASCII
            new_ascii = position + shift_base

            # Convert ASCII to character
            encrypted_char = chr(new_ascii)

            # Add encrypted letter
            encrypted_text += encrypted_char

        else:
            # Keep spaces, numbers and symbols unchanged
            encrypted_text += char

    return encrypted_text


# ------------------ Decryption Function ------------------

def caesar_cipher_decrypt(text, shift):

    decrypted_text = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                shift_base = ord("A")
            else:
                shift_base = ord("a")

            position = ord(char) - shift_base

            position = position - shift

            position = position % 26

            new_ascii = position + shift_base

            decrypted_char = chr(new_ascii)

            decrypted_text += decrypted_char

        else:
            decrypted_text += char

    return decrypted_text


# ------------------ Main Program ------------------

encrypted_text = caesar_cipher_encrypt(text, shift)

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)

print("===================================")
print("Encrypted Text :", encrypted_text)
print("Decrypted Text :", decrypted_text)
print("===================================")
print("Thank you for using Caesar Cipher Encryptor!")