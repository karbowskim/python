#Cryptopals challenge 3
import binascii
import base64

#TODO: use scoring function to pick the plaintext

def byteXor(string1, string2):
    return bytes([_x ^ _y for _x,_y in zip(string1, string2)])

def getKey(character, length):
    keyString = ''
    for i in range (0, length):
        keyString += chr(character)
    return keyString

def get_english_score(input_bytes):
    #Borrowed from: https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/
    """Compares each input byte to a character frequency 
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """

    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' ', which I estimated.
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


cipherText = input("Ciphertext: ")
cipherTextDecoded = binascii.unhexlify(cipherText)

for character in range(65, 90):
    keyString = getKey(character, len(cipherTextDecoded))
    xored = byteXor(cipherTextDecoded, keyString.encode('ascii'))
    plaintext = xored.decode("utf-8")
    print (chr(character) + " - " + plaintext)