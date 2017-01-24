import xorly
import binascii

def getDist(word1, word2):
    return sum([bin(ord(word1[i]) ^ ord(word2[i])).count('1') for i in range(len(word1))])

testPhrase1 = "this is a test"
testPhrase2 = "wokka wokka!!!"

print(getDist(testPhrase1, testPhrase2))
#print(binascii.a2b_uu('a'))