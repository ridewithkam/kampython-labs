class Caesar:
    def __init__(self, key=0):
        self._key = key

    def set_key(self, key):
        self._key = key
    
    def get_key(self):
        return self._key

    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    shifted = ord(char) + self._key
                    ciphertext += chr((shifted - ord('a')) % 26 + ord('a'))
                else:
                    shifted = ord(char) + self._key
                    ciphertext += chr((shifted - ord('A')) % 26 + ord('A'))
            elif char.isspace():
                ciphertext += char
            else:
                ciphertext += chr((ord(char) + self._key) % 128)
        return ciphertext
    
    def decrypt (self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    shifted = ord(char) - self._key
                    plaintext += chr((shifted - ord('a')) % 26 + ord('a'))
                else:
                    shifted = ord(char) - self._key
                    plaintext += chr((shifted - ord('A')) % 26 + ord('A'))
            elif char.isspace():
                plaintext += char
            else:
                plaintext += chr((ord(char) - self._key) % 128)
        return plaintext

cipher = Caesar()
cipher.set_key(3)

print(cipher.encrypt("Where ya mom at"))
print(cipher.decrypt("Zkhuh bd prp dw"))

## alright bye byee!