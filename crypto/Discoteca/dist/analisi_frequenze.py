#!/usr/bin/env python3

with open("plaintext.txt", "r") as f:
    plaintext = f.read()
    f.close()

def analyze(text) -> dict:
    freq:dict = {}
    # Count the frequency of each character
    freq['{'] = 1.0
    freq['}'] = 1.0
    for c in text:
        if c in 'áàäâãåéèëêíìïîóòöôõúùüûñçÁÀÄÂÃÅÉÈËÊÍÌÏÎÓÒÖÔÕÚÙÜÛÑÇ':
            c = c.translate(str.maketrans('áàäâãåéèëêíìïîóòöôõúùüûñçÁÀÄÂÃÅÉÈËÊÍÌÏÎÓÒÖÔÕÚÙÜÛÑÇ', 'aaaaaaeeeeiiiiooooouuuuncAAAAAAEEEEIIIIOOOOOUUUUNC'))
        if c in freq:
            freq[c] += 1.0
        else:
            freq[c] = 1.0
    # Normalize the frequency
    for c in freq:
        freq[c] *= 100/len(text)
    return freq

frequencies:dict = analyze(plaintext)
with open('frequencies.txt', 'w') as f:
    for key, value in frequencies.items():
        k = str(key).encode('utf-8').hex()
        f.write(k + ' : ' + str(value) + '\n')
    f.close()
