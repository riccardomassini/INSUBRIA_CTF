#!/usr/bin/env python3

def encrypt(plain:str, shift:int) -> str:
    encrypted = []
    for char in plain:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            #encrypted.append(char)
            pass
    return ''.join(encrypted)

def decrypt(cipher:str, shift:int) -> str:
    return encrypt(cipher, -shift)

def main():
    with open("lorem.txt", "r") as f:
        lorem = f.read()
        f.close()
    secret = lorem
    shift = 24
    encrypted = encrypt(secret.upper(), shift)
    print(encrypted)
    with open("morituri.enc", "w") as f:
        f.write(encrypted)
        f.close()

if __name__ == "__main__":
    main()