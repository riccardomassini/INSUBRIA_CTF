enc_flag = "".join([hex((ord(el) ^ 42) ^ k)[2:].zfill(2) for el in "flag{REDACTED}"] if (k := __import__("random").randint(1,200)) else [])

# enc_flag = "ede7eaecf0bbe5b8d4e7bae5b8f9d4e8f9f2fbffbbd4e6bff8ffb8f9f6"