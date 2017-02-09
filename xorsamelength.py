import binascii
import hextobase64

def xorBytes(s, k):
    return "".join(chr(s[i] ^ k[i%len(k)]) for i in range(0, len(s)))