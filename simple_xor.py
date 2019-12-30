#simple xor
import binascii
import base64

key = "secret_key"
text = input("Input plaintext: ")

def simpleXor(key, data):
    key = bytearray(key, encoding='utf8')
    data = bytearray(data, encoding='utf8')

    output = []
    for i, d in enumerate(data):
        output.append(chr(d ^ key[i % len(key)]))
        print(output)
    return ''.join(output)

cipherText = simpleXor(text, key)
print(text)
print(cipherText)