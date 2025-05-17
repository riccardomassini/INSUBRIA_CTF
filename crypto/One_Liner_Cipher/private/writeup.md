# One Linear Cipher

## Overview
To get the flag, you need to reverse the function by brute forcing all possible values of k (from 1 to 200).

## Exploit
```py
enc_flag = "ede7eaecf0bbe5b8d4e7bae5b8f9d4e8f9f2fbffbbd4e6bff8ffb8f9f6"
k_range = 200

for k in range(1, k_range + 1):
    try:
        flag = "".join([chr((int(enc_flag[i:i+2], 16) ^ k) ^ 42) for i in range(0, len(enc_flag), 2)])
        if flag.startswith("flag{"):
            print(flag)
            break
    except:
        pass
```