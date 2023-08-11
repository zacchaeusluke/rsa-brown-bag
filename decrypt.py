import secret
from math import prod
from Crypto.Util.number import long_to_bytes
from sympy import integer_nthroot

messages = [secret.get_secret() for _ in range(3)]

def crt(m, n):
    N = prod(n)
    y = [N // n_i for n_i in n]
    # multiplicative inverses
    z = [pow(y_i, -1, n_i) for y_i, n_i in zip(y, n)]
    return sum(a_i * y_i * z_i for a_i, y_i, z_i in zip(m, y, z)) % N

def get_int(d):
    return int(d, 16)

m = [get_int(m['message']) for m in messages]
n = [get_int(m['public_key'][0]) for m in messages]
e = int(messages[0]['public_key'][1])

x = crt(m, n)

answer = integer_nthroot(x, e)
answer = long_to_bytes(answer[0]).decode('utf-8')

print(answer)