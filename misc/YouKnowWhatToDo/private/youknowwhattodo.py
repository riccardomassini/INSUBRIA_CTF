#!/usr/bin/env python3
import numpy as np
from PIL import Image

flag = "who_is_the_boss.png"
bob = "bob_ross.png"


im1 = Image.open(flag)
im2 = Image.open(bob)

im1np = np.array(im1)*255
im2np = np.array(im2)*255

enc1 = np.bitwise_xor(im1np, im2np).astype(np.uint8)
Image.fromarray(enc1).save('flag_enc.png')
