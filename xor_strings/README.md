
## Description
Suprisingly Python doesn't seem to have a straigtforward way or xor'ing two strings. Going off some examples I found line, I put together a simple tool I could use. This is easier in other languages like ruby, but it gave me something to hack on and this was the result.

## Usage
```
Usage: xor_strings.py [OPTIONS]

  xors any combination of two hexidecmal or plaintext strings

Options:
  -x, --hexidecimal TEXT  a hexidecimal string to xor; this option can be
                          repeated
  -s, --string TEXT       a string to xor; this option can be repeated
  --help                  Show this message and exit.
```

## Example

This example shows a piped usage intended to solve a one time pad challenge
```
$> python xor_strings.py  -x 6c73d5240a948c86981bc294814d -s 'attack at dawn' | xargs -I{} python xor_strings.py -x {} -s 'attack at dusk'
6c73d5240a948c86981bc2808548
$>
```
