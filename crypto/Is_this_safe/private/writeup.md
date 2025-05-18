# Is this safe?

## Cipher analilsis
The cipher takes in input a string and a number between 2 and 8912.
Since the number of keys is small we can try all of them.
The cipher simply multiply the letter of the plaintext by the key.
To decipher the plain text we divide the character by the key.
Try all the key until you get a plaintext with `flag` at the beginning.
