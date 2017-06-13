#!/usr/bin/env python

from binascii import unhexlify, hexlify
import click
import sys


def xor_strings(s, t):
    """
    xor two strings together by first getting their ascii code values
    and then xor'ing them
    """
    # ord returns an integer of the ascii code of a given one char string
    # chr returns a one char string from a given ascii code value
    # hexlify turns the given string into a hex string
    return hexlify(''.join(chr(ord(a)^ord(b)) for a, b in zip(s, t)))


@click.command()
@click.option('--hexidecimal', '-x', multiple=True, help='a hexidecimal string to xor; this option can be repeated')
@click.option('--string', '-s', multiple=True, help='a string to xor; this option can be repeated')
def xor(hexidecimal, string):
    """
    xors any combination of two hexidecmal or plaintext strings
    """
    str1 = None
    str2 = None
    # hexlify turns the plain string into hex in string form
    string = [unhexlify(h) for h in hexidecimal] + list(string)

    # only use 2 args
    if len(string) != 2:
        print('Need to specificy only two strings to xor.')
        sys.exit(2)
    else:
        str1, str2 = string[:2]
    xord = xor_strings(str1, str2)
    print(xord)


if __name__ == '__main__':
    xor()

