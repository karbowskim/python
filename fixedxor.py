#Cryptopals challenge 2
import binascii
import base64

buffferOne = raw_input("Buffer 1: ")
buffferTwo = raw_input("Buffer 2: ")

bufferOneHexDecoded = binascii.unhexlify(buffferOne)
bufferTwoHexDecoded = binascii.unhexlify(buffferTwo)
xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(bufferOneHexDecoded, bufferTwoHexDecoded))

print("Xored: " + binascii.hexlify(xored))