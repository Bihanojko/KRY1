#!/usr/bin/python3

# Project 1
# Cryptography
# Nikola Valesova, xvales02


import sys
from satispy import Variable, Cnf 
from satispy.solver import Minisat
 
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


def arrayToInt(solution, variables):
    intFromArray = 0
    for idx in range(N):
        if solution[variables[(idx + 1) % N]] == True:
            intFromArray |= 1 << idx
        else:
            intFromArray |= 0 << idx            
    return intFromArray


def reversedStep(x):
    variables = []
    for i in range(N):
        variables.append(Variable(str(i)))

    exp = Variable('None')

    for i in range(N):
        if (x >> i) & 1:
            exp &= (variables[i] & -variables[(i + 1) % N] & -variables[(i + 2) % N]) | (-variables[i] & variables[(i + 1) % N]) | (-variables[i] & variables[(i + 2) % N])
        else:
            exp &= (-variables[i] & -variables[(i + 1) % N] & -variables[(i + 2) % N]) | (variables[i] & variables[(i + 1) % N]) | (variables[i] & variables[(i + 2) % N])

    solver = Minisat()
    solution = solver.solve(exp)
    if solution.success:
        return arrayToInt(solution, variables)


# Keystream init
keystr = int.from_bytes(keystream, 'little')

for _ in range(N // 2):
    keystr = reversedStep(keystr)

# print secret key
keystr = keystr.to_bytes(N_B, 'little')
keystr = keystr.decode("ascii")
print(''.join([x for x in keystr if x.isprintable()]), end='')
