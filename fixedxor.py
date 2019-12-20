#Cryptopals challenge 2
import binascii
import base64

def byteXor(string1, string2):
    return bytes([_x ^ _y for _x,_y in zip(string1, string2)])

buffferOne = input("Buffer 1: ")
buffferTwo = input("Buffer 2: ")

bufferOneHexDecoded = binascii.unhexlify(buffferOne)
bufferTwoHexDecoded = binascii.unhexlify(buffferTwo)

xored = byteXor(bufferOneHexDecoded, bufferTwoHexDecoded)

print(binascii.hexlify(xored).decode("utf-8"))