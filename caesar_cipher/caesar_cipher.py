#!/bin/python3

"""
Caesar Cipher Implmentation
"""

import sys
import click


def apply_rotation(c, factor):
    """Applies a shift of factor to the letter denoted by c"""
    if c.isalpha():
        lower = ord('A') if c.isupper() else ord('a')
        c = chr(lower + ((ord(c) - lower + factor) % 26))
    return c


def caesar_cipher(s, k):
    """Iterates through each letter and constructs the cipher text"""
    new_message = ''
    factor = k % 26
    for c in s:
        new_message += apply_rotation(c, factor)
    return new_message


@click.command()
@click.argument('text', type=str)
@click.argument('factor', type=int)
def caesar(text, factor):
    """
    \b
    text - the string to apply the caesar cipher to
    factor - int for how many rotations to apply to each char
    """
    print(caesar_cipher(text, factor))


if __name__ == '__main__':
    caesar()
