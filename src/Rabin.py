import src.prime as prime
import numpy as np


def encryption(plaintext, n):
    plaintext = padding (plaintext)
    return (plaintext ** 2) * (n-1) % n


def padding(plaintext):
    binary_str = bin(plaintext)
    binary_str += bin(int(np.mean([ord(ch) for ch in 'paddingbytes'])))[2:]

    return int (binary_str, 2)


def decryption(a, p, q):
    n = p * q

    r = pow(a, (p + 1) // 4, p)
    s = pow(a, (q + 1) // 4, q)

    gcd, c, d = prime.egcd (p, q)
    x = (r * d * q + s * c * p) % n
    y = (r * d * q - s * c * p) % n
    lst = [x, n - x, y, n - y]

    plaintext = choose(lst)

    return plaintext


def choose(lst):
    for i in lst:
        binary = bin(i)
        padding = bin(int(np.mean([ord(ch) for ch in 'paddingbytes'])))[2:]

        if binary[-len(padding):] == padding:
            return int(binary[:-len(padding)],2)

    return ord('?')
