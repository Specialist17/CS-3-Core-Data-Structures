#!python

import string
import math
import pdb
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
characters = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 4: "4", 5: "5", 6: "6",
              7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E",
              15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K", 21: "L",
              22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R", 28: "S",
              29: "T", 30: "U", 31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z", }

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    binary_list = []
    current_quotient = number
    binary_list.append(str(characters[current_quotient % base].lower()))
    while math.floor(current_quotient/base) > 0:
        current_quotient = math.floor(current_quotient/base)
        binary_list.append(str(characters[current_quotient % base].lower()))
    return "".join(binary_list[::-1])


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


def encode_binary():
    # assert encode(0, 2) == '0'  # Should '' be valid?
    print(encode(1, 2) == '1')
    print(encode(2, 2) == '10')
    print(encode(3, 2) == '11')
    print(encode(4, 2) == '100')
    print(encode(5, 2) == '101')
    print(encode(6, 2) == '110')
    print(encode(7, 2) == '111')
    print(encode(8, 2) == '1000')
    print(encode(9, 2) == '1001')
    print(encode(10, 2) == '1010')
    print(encode(11, 2) == '1011')
    print(encode(12, 2) == '1100')
    print(encode(13, 2) == '1101')
    print(encode(14, 2) == '1110')
    print(encode(15, 2) == '1111')
    print(encode(248975, 2) == '111100110010001111')


def encode_hexadecimal():
    print(encode(10, 16) == 'a')
    print(encode(15, 16) == 'f')
    print(encode(153, 16) == '99')
    print(encode(255, 16) == 'ff')
    print(encode(2766, 16) == 'ace')
    print(encode(3243, 16) == 'cab')
    print(encode(48813, 16) == 'bead')
    print(encode(64206, 16) == 'face')
    print(encode(12648430, 16) == 'c0ffee')
    print(encode(16435934, 16) == 'facade')
    print(encode(3735928559, 16) == 'deadbeef')
    print(encode(4027038225, 16) == 'f007ba11')


def encode_1234():
    print(encode(1234, 2) == '10011010010')
    print(encode(1234, 3) == '1200201')
    print(encode(1234, 4) == '103102')
    print(encode(1234, 5) == '14414')
    print(encode(1234, 8) == '2322')
    print(encode(1234, 10) == '1234')
    print(encode(1234, 16) == '4d2')
    print(encode(1234, 32) == '16i')


def encode_248975():
    print(encode(248975, 2) == '111100110010001111')
    print(encode(248975, 4) == '330302033')
    print(encode(248975, 8) == '746217')
    print(encode(248975, 10) == '248975')
    print(encode(248975, 16) == '3cc8f')
    print(encode(248975, 25) == 'fn90')
    print(encode(248975, 32) == '7j4f')
    print(encode(248975, 36) == '5c3z')


def encode_into_10():
    print(encode(2, 2) == '10')
    print(encode(4, 4) == '10')
    print(encode(8, 8) == '10')
    print(encode(10, 10) == '10')
    print(encode(16, 16) == '10')
    print(encode(25, 25) == '10')
    print(encode(32, 32) == '10')
    print(encode(36, 36) == '10')


def encode_into_1010():
    print(encode(10, 2) == '1010')
    print(encode(68, 4) == '1010')
    print(encode(520, 8) == '1010')
    print(encode(1010, 10) == '1010')
    print(encode(4112, 16) == '1010')
    print(encode(15650, 25) == '1010')
    print(encode(32800, 32) == '1010')
    print(encode(46692, 36) == '1010')

if __name__ == '__main__':
    # main()
    encode_binary()
    encode_hexadecimal()
    encode_1234()
    encode_248975()
    encode_into_10()
    encode_into_1010()
