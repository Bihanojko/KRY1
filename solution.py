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
SUB = [0, 1, 1, 0, 1, 0, 1, 0]
N_B = 32
N = 8 * N_B


def getNext(currBit, i1, i2):
    # print(str(currBit) + " , " + str(i1) + " , " + str(i2))
    if currBit == 0:
        if i1 == i2 == 0:
            return 0
        else:
            return 1
    else:
        if i1 == i2 == 0:
            return 1
        else:
            return 0


def arrayToInt(x):
    intFromArray = 0
    for idx in range(len(x)):
        if idx != 0 and idx != len(x) - 1:
            intFromArray |= x[idx] << (N - idx)
    return intFromArray


def reversedStep(x):
    for seq in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        keyArray = seq
        for i in range(N):
            currBit = (x >> (N - i - 1)) & 1
            keyArray.append(getNext(currBit, keyArray[i + 1], keyArray[i]))
        # print(arrayToInt(keyArray))
        if (keyArray[0] == keyArray[N] and keyArray[1] == keyArray[N + 1]):
            return arrayToInt(keyArray)


# Keystream init
keystr = int.from_bytes(keystream, 'little')

for _ in range(N // 2):
    keystr = reversedStep(keystr)

# print secret key
keystr = keystr.to_bytes(N_B, 'little')
keystr = keystr[:29]
print(keystr.decode("ascii"))
