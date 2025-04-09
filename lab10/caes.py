## lets work
def shift_char(c, shift):
    if c.isupper():
        return chr((ord(c) - 65 + shift) % 26 + 65)
    elif c.islower():
        return chr((ord(c) - 97 + shift) % 26 + 97)
    else:
        return c

def caesar_cipher(text, shift):
    return ''.join(shift_char(c, shift) for c in text)

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def main():
    message = "Hi, it's Kam!"
    shift_amount = 3

    encrypted_message = caesar_cipher(message, shift_amount)
    decrypted_message = caesar_decipher(encrypted_message, shift_amount)

    print("Original Message:", message)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
