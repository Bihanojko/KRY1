#!/usr/bin/python3

import sys
 
# read input files as byte arrays
plaintext = bytearray(open('./in/bis.txt', 'rb').read())
ciphertext = bytearray(open('./in/bis.txt.enc', 'rb').read())
 
# set the length to be the size of the smaller file
size = len(plaintext) if plaintext < ciphertext else len(ciphertext)
keystream = bytearray(size)

# XOR the plaintext and ciphertext files
for i in range(size):
	keystream[i] = plaintext[i] ^ ciphertext[i]

keystream = bytearray(keystream)
# get first 32 characters of keystream
keystream = keystream[:32]


# key scheduling algorithm
SUB = [0, 1, 1, 0, 0, 1, 0, 1]
N_B = 32
N = 8 * N_B

# Next keystream
def step(x):
    x = (x & 1) << N+1 | x << 1 | x >> N-1
    y = 0
    for i in range(N):
        y |= SUB[(x >> i) & 7] << i
    return y

# Keystream init
keystr = int.from_bytes(keystream, 'little')
for i in range(N//2):
    keystr = step(keystr)

# print secret key
print((keystr.to_bytes(N_B, 'little')).decode("utf-8"))
sys.exit(0)
