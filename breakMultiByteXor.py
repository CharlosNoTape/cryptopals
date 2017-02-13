import breaksinglebytexor
import xorsamelength
import textwrap
import binascii

phrase1 = b"this is a test"
phrase2 = b"wokka wokka!!!"

f = open("crypt6.txt", "rU")
crypt = ''.join(f.read().splitlines())
crypt = binascii.a2b_base64(crypt)
f.close()

print(crypt)

def hammingDist(c, r):
    return sum([bin(a ^ b).count('1') for a, b in zip(c, r)])

def chop(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def normalHam(s, k):
    samp1 = s[:k]
    samp2 = s[k:2*k]
    samp3 = s[2*k:3*k]
    samp4 = s[3*k:4*k]
    return (hammingDist(samp1, samp2) + hammingDist(samp3, samp4))/4

def breakAny(s):
    keylist = []
    for k in range(2, 41):
        keylist.append((k, normalHam(s, k)))
    def getKey(s):
        return s[-1]
    keylist = sorted(keylist, key=getKey)
    keylength = keylist[0][0]
    parts = chop(s, keylength)
    print(parts)
    segments = []
    for i in range(keylength):
        segments.append(b''.join([part[i] for part in parts]))
    print(segments)
    return

breakAny(crypt)