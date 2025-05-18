#!/usr/bin/env python3

with open("flag.txt", "r") as f:
    flag:str = f.read().strip()
    f.close()
with open("key.txt", "r") as f:
    key:int = int(f.read().strip())
    f.close()

def cipher(message:str, key:int) -> str:
    if key < 2 and key > 8912:
        return message
    ciphertext:str = ""
    for letter in message:
        ciphertext += chr(ord(letter) * key)
    return ciphertext

def main():
    ciphertext:str = cipher(message=flag, key=key)
    print(ciphertext)

if __name__ == "__main__":
    main()
