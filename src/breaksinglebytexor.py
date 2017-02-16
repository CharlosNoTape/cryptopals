import xorsamelength
import binascii

freq = {
    'a': 7.52766,
    'e': 7.0925,
    'o': 5.17,
    'r': 4.96032,
    'i': 4.69732,
    's': 4.61079,
    'n': 4.56899,
    '1': 4.35053,
    't': 3.87388,
    'l': 3.77728,
    '2': 3.12312,
    'm': 2.99913,
    'd': 2.76401,
    '0': 2.74381,
    'c': 2.57276,
    'p': 2.45578,
    '3': 2.43339,
    'h': 2.41319,
    'b': 2.29145,
    'u': 2.10191,
    'k': 1.96828,
    '4': 1.94265,
    '5': 1.88577,
    'g': 1.85331,
    '9': 1.79558,
    '6': 1.75647,
    '8': 1.66225,
    '7': 1.621,
    'y': 1.52483,
    'f': 1.2476,
    'w': 1.24492,
    'j': 0.836677,
    'v': 0.833626,
    'z': 0.632558,
    'x': 0.573305,
    'q': 0.346119,
    'A': 0.130466,
    'S': 0.108132,
    'E': 0.0970865,
    'R': 0.08476,
    'B': 0.0806715,
    'T': 0.0801223,
    'M': 0.0782306,
    'L': 0.0775594,
    'N': 0.0748134,
    'P': 0.073715,
    'O': 0.0729217,
    'I': 0.070908,
    'D': 0.0698096,
    'C': 0.0660872,
    'H': 0.0544319,
    'G': 0.0497332,
    'K': 0.0460719,
    'F': 0.0417393,
    'J': 0.0363083,
    'U': 0.0350268,
    'W': 0.0320367
}

def score(s):
    score = 0
    for c in s:
        if c in freq:
            score += freq[c]
    return score

#List all possible results
def breakSingle(s):
    ciphertext = []
    for k in range(0, 127):
        xoredtext = xorsamelength.xorBytes(s, bytes([k]))
        ciphertext.append((xoredtext, chr(k), score(xoredtext)))
    def getKey(s):
        return s[-1]
    ciphertext = sorted(ciphertext, key=getKey)
    s = ciphertext[-1][0]
    return s

crypt = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

#ciphertext = breakSingleByteXor(binascii.unhexlify(crypt))

print(breakSingle(binascii.unhexlify(crypt)))