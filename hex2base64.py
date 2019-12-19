#Cryptopals challenge 1

import binascii
import base64

hexInput = raw_input("Input hex string: ")
base64Output = base64.b64encode(binascii.unhexlify(hexInput))
print("Base64: " + base64Output)