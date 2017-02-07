import binascii
import hextobase64

given = "1c0111001f010100061a024b53535009181c"
xorkey = "686974207468652062756c6c277320657965"
expected = "746865206b696420646f6e277420706c6179"

def xorstring(original, key):
    return "".join(chr(a ^ b) for a, b in zip(binascii.unhexlify(original), binascii.unhexlify(key)))

print (xorstring(given, xorkey))
print (expected)