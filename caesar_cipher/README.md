# Description
This is just an example implementation of the Caeser Cipher. The cipher picks
a rotation factor and rotates each letter by that factor. For example, if our
factor was 3 and we had the letter 'a', we could apply the cipher by adding 3
to 'a' to give us 'd'. If we applied it to a longer string like "cat", we
would get "fdw".

# Usage:
Usage: caesar_cipher.py [OPTIONS] TEXT FACTOR

  text - the string to apply the caesar cipher to
  factor - int for how many rotations to apply to each char

Options:
  --help  Show this message and exit.

# Examples

```
$> python3 caesar_cipher.py cat 3
fdw
$> python3 caesar_cipher.py -- fdw -3
cat
```
