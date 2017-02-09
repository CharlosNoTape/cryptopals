import binascii
import hextobase64

#given = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
#xorkey = bytes([97])
#expected = "746865206b696420646f6e277420706c6179"

#def xorSameLengthString(original, key):
#    return "".join(chr(a ^ b) for a, b in zip(binascii.unhexlify(original), binascii.unhexlify(key)))

#def xorOneByteKey(original, k):
#    return "".join(chr(a ^ k) for a in binascii.unhexlify(original))

def xorBytes(s, k):
    return "".join(chr(s[i] ^ k[i%len(k)]) for i in range(0, len(s)))

#print(ord(xorkey))
#print (xorBytes(binascii.unhexlify(given), xorkey))