import binascii

def hex2b64(h):
    return str(binascii.b2a_base64(binascii.a2b_hex(h)))

def str2hex(s):
    return str(binascii.b2a_hex(binascii.a2b_uu(s)))

#given = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
#expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

#print ("Result = %s" % hextobase64(given))
#print ("Expected = %s" % expected)