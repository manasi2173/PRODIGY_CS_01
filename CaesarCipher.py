def encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)


def main():
    message = input("Enter a message: ")
    shift = int(input("Enter a shift value: "))

    encrypted_message = encrypt(message, shift)
    decrypted_message = decrypt(encrypted_message, shift)

    print("\nEncrypted Message: ", encrypted_message)
    print("Decrypted Message: ", decrypted_message)

if __name__ == "__main__":
    main()



