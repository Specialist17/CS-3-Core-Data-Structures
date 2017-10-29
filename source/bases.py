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
ENCODING_CHARACTERS = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 4: "4", 5: "5", 6: "6",
              7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E",
              15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K", 21: "L",
              22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R", 28: "S",
              29: "T", 30: "U", 31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z", }
DECODING_CHARACTERS = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "4": 4, "5": 5, "6": 6,
              "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12 , "d": 13 , "e": 14 ,
              "f": 15 , "g": 16 , "h": 17 , "i": 18 , "j": 19 , "k": 20 , "l": 21 ,
              "m": 22 , "n": 23 , "o": 24 , "p": 25 , "q": 26 , "r": 27 , "s": 28 ,
              "t": 29 , "u": 30 , "v": 31 , "w": 32 , "x": 33 , "y": 34 , "z": 35 }

## TODO: do it in 4 lines
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
            value = level * int(DECODING_CHARACTERS[digit])
        else:
            value = level * int(digit)
        total_sum += int(value)
        level = level * base
    return total_sum


## TODO: do it in 5 lines, maybe down to 3
def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    digit_list = []
    current_quotient = number
    digit_list.append(str(ENCODING_CHARACTERS[current_quotient % base].lower()))
    while math.floor(current_quotient/base) > 0:
        current_quotient = math.floor(current_quotient/base)
        digit_list.append(str(ENCODING_CHARACTERS[current_quotient % base].lower()))
    return "".join(digit_list[::-1])


def encode_fractional(number, base, precision):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # separate integer from decimal numbers
    base_number = str(number).split(".")
    decimal_num = encode(int(base_number[0]), base)

    fraction_list = []

    # create a decimal number with the decimal extracted from base_number
    current_multiple = float("0." + base_number[1])

    for _ in range(precision):
        # multiply the current decimal by the base
        current_multiple = current_multiple * base

        # get the current integer value
        fractional_binary = str(current_multiple).split(".")[0]
        fraction_list.append(ENCODING_CHARACTERS[int(fractional_binary)].lower())

        # reset the integer value to 0
        current_multiple = float("0." + str(current_multiple).split(".")[1])

    final_binary = decimal_num + "." + "".join(fraction_list)
    return final_binary


def decode_fractional(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # separate integer from decimal numbers
    base_number = digits.split(".")
    assert len(base_number) <= 2, 'too many decimal points {}'.format(len(base_number))


    decimal_num = decode(base_number[0], base)
    fractional_num = base_number[1]

    # create a decimal number with the decimal extracted from base_number
    current_multiple = 0

    for power, decimal in enumerate(fractional_num):
        # divide the current decimal by the base elevated to the current power
        current_multiple += int(DECODING_CHARACTERS[decimal])/(base ** (int(power)+1))
    #
    final_binary = decimal_num + current_multiple
    return final_binary


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

    if base1 == 10:
        return encode(int(digits), base2)
    else:
        base_10_repr = decode(digits, base1)
        return encode(base_10_repr, base2)

def convert_fractional(digits, base1, base2, precision):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)

    if base1 == 10:
        return encode_fractional(int(digits), base2, precision)
    else:
        base_10_repr = decode_fractional(digits, base1)
        return encode_fractional(base_10_repr, base2, precision)


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


if __name__ == '__main__':
    main()
    # print(encode_fractional(4.5374, 2, 10))
    # print(encode_fractional(46.712837, 16, 10))
    # print(decode_fractional('10.1011011001', 2))
    # print(decode_fractional('11010.11010100001', 2))
    # print(decode_fractional('111111.100011100', 2))
    # print(decode_fractional('111111.100011100', 5) == 3906.2003968)
    # print(decode_fractional('f42.334d3466', 16))

    print(convert_fractional('1101.11010100001', 2, 16, 3))
    print(convert_fractional('1011.100101', 2, 16, 3))
    print(convert_fractional('1100.10100001', 2, 16, 3))
    print(convert_fractional('1101.111', 2, 16, 3))
    print(convert_fractional('1110.11000', 2, 8, 3))
    print(convert_fractional('1111.101010', 2, 12, 3))
    # print(convert_fractional('1100100001000000', 2, 16) == 'c840')
    # print(convert_fractional('1101100101010001', 2, 16) == 'd951')
    # print(convert_fractional('1110101001100010', 2, 16) == 'ea62')
    # print(convert_fractional('1111101101110011', 2, 16) == 'fb73')
