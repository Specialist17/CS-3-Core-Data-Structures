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
encoding_characters = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 4: "4", 5: "5", 6: "6",
              7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E",
              15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K", 21: "L",
              22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R", 28: "S",
              29: "T", 30: "U", 31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z", }
decoding_characters = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "4": 4, "5": 5, "6": 6,
              "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12 , "d": 13 , "e": 14 ,
              "f": 15 , "g": 16 , "h": 17 , "i": 18 , "j": 19 , "k": 20 , "l": 21 ,
              "m": 22 , "n": 23 , "o": 24 , "p": 25 , "q": 26 , "r": 27 , "s": 28 ,
              "t": 29 , "u": 30 , "v": 31 , "w": 32 , "x": 33 , "y": 34 , "z": 35 }

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    digits_list = digits[::-1]
    level = 1
    total_sum = 0
    for digit in digits_list:
        if base > 10:
            value = level * int(decoding_characters[digit])
        else:
            value = level * int(digit)
        total_sum += int(value)
        level = level * base

    print(total_sum)
    return total_sum
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
    digit_list = []
    current_quotient = number
    digit_list.append(str(encoding_characters[current_quotient % base].lower()))
    while math.floor(current_quotient/base) > 0:
        current_quotient = math.floor(current_quotient/base)
        digit_list.append(str(encoding_characters[current_quotient % base].lower()))
    return "".join(digit_list[::-1])


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


def decode_binary():
    print(decode('0', 2) == 0)
    print(decode('1', 2) == 1)
    print(decode('10', 2) == 2)
    print(decode('11', 2) == 3)
    print(decode('100', 2) == 4)
    print(decode('101', 2) == 5)
    print(decode('110', 2) == 6)
    print(decode('111', 2) == 7)
    print(decode('1000', 2) == 8)
    print(decode('1001', 2) == 9)
    print(decode('1010', 2) == 10)
    print(decode('1011', 2) == 11)
    print(decode('1100', 2) == 12)
    print(decode('1101', 2) == 13)
    print(decode('1110', 2) == 14)
    print(decode('1111', 2) == 15)

def decode_decimal():
    print(decode('5', 10) == 5)
    print(decode('9', 10) == 9)
    print(decode('10', 10) == 10)
    print(decode('25', 10) == 25)
    print(decode('64', 10) == 64)
    print(decode('99', 10) == 99)
    print(decode('123', 10) == 123)
    print(decode('789', 10) == 789)
    print(decode('2345', 10) == 2345)
    print(decode('6789', 10) == 6789)
    print(decode('13579', 10) == 13579)
    print(decode('24680', 10) == 24680)

def decode_hexadecimal():
    print(decode('a', 16) == 10)
    print(decode('f', 16) == 15)
    print(decode('99', 16) == 153)
    print(decode('ff', 16) == 255)
    print(decode('ace', 16) == 2766)
    print(decode('cab', 16) == 3243)
    print(decode('bead', 16) == 48813)
    print(decode('face', 16) == 64206)
    print(decode('c0ffee', 16) == 12648430)
    print(decode('facade', 16) == 16435934)
    print(decode('deadbeef', 16) == 3735928559)
    print(decode('f007ba11', 16) == 4027038225)

if __name__ == '__main__':
    # main()
    # encode_binary()
    # encode_hexadecimal()
    # encode_1234()
    # encode_248975()
    # encode_into_10()
    # encode_into_1010()
    decode_binary()
    decode_decimal()
    decode_hexadecimal()
