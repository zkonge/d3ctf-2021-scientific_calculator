# d3ctf-2021-scientific_calculator

This is a archive of the challenge "scientific calculator" in D^3CTF 2021.

## Environment

`Python 3.9.1+` from Debian bullseye (testing) package manager in 2021/3/7.

In fact, `Python3.9.1+` nearly equals to `Python3.9.2`, both of them fixed same security vulnerabilities.

For this challenge, The `Python 3.9.2` from Docker Hub may not works properly, because of its strange dynamic libraries.

## Deployment

Just run `python calculator.py`

## Challenge description

This is a super-safe and powerful scientific calculator.

```python3
import cmath

# you can play with complex number
n = 1 + 1j
n = cmath.log(n ** 4)
print(n)

# ... and definite integral
f = lambda x: x ** 2
bottom = 0
top = 1

result = 0
unit = 1e-5

while bottom < top:
    result += f(bottom) * unit
    bottom += unit

print(result)

# but you can't control my server :P
# import os
# os.system('/bin/sh')
```

## Solution

Waiting for *PSRT* 's response...