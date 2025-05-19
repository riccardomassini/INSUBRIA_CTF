#!/bin/python3

import random
import string

def gen_dictionary() -> dict:
    d:dict = {}
    used:list = []
    length = len(string.printable)
    for char in string.printable:
        l:int = random.randint(0, length-1)
        while l in used:
            l = (l+1) % length
        used.append(l)
        d[char] = string.printable[l]
    return d

def insert_flag(flag:str, text:str) -> str:
    i:int = random.randint(0, len(text)-1)
    return text[:i] + flag + text[i:]

def cipher(text:str, dictionary:dict) -> str:
    cipher = ""
    for char in text:        
        if char in 'áàäâãåéèëêíìïîóòöôõúùüûñçÁÀÄÂÃÅÉÈËÊÍÌÏÎÓÒÖÔÕÚÙÜÛÑÇ':
            char = char.translate(str.maketrans('áàäâãåéèëêíìïîóòöôõúùüûñçÁÀÄÂÃÅÉÈËÊÍÌÏÎÓÒÖÔÕÚÙÜÛÑÇ', 'aaaaaaeeeeiiiiooooouuuuncAAAAAAEEEEIIIIOOOOOUUUUNC'))
        if char in dictionary:
            cipher += dictionary[char]
        else:
            cipher += char
    return cipher

def decipher(text:str, dictionary:dict) -> str:
    plain = ""
    for char in text:
        if char not in string.printable:
            plain += char
        else:
            for key, value in dictionary.items():
                if value == char:
                    plain += key
                    break
    return plain


dictionary:dict = gen_dictionary()
'''
with open('dictionary.txt', 'w') as f:
    for key, value in dictionary.items():
        k = str(key).encode('utf-8').hex()
        v = str(value).encode('utf-8').hex()
        f.write(k + ':' + v + '\n')
    f.close()
'''

with open('dictionary.txt', 'r') as f:
    dictionary:dict = {}
    for line in f:
        k, v = line.strip().split(':')
        key = bytes.fromhex(k).decode('utf-8')
        value = bytes.fromhex(v).decode('utf-8')
        dictionary[key] = value
    f.close()


with open('flag.txt', 'r') as f:
    flag:str = f.read().strip()
    f.close()

with open('plaintext.txt', 'r') as f:
    plaintext:str = f.read().strip()
    f.close()

text:str = insert_flag(flag, plaintext)

ciphertext:str = cipher(text, dictionary)

with open('ciphertext.txt', 'w') as f:
    f.write(ciphertext)
    f.close()        
