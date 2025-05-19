enc_flag = "".join([hex((ord(el) ^ 42) ^ k)[2:].zfill(2) for el in "flag{0n3_l1n3r_crypt0_m4st3r}"] if (k := __import__("random").randint(1,200)) else [])

print(f"enc_flag = {enc_flag}")