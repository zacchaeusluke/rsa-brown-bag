from math import gcd
from Crypto.Util.number import bytes_to_long, getPrime

with(open('super_secret_message.txt', 'r')) as f:
    super_secret_message = f.read()

bit_size = 2048
e = 3

def get_new_public_key(bit_size, e):
    while True:
        p = getPrime(bit_size // 2)
        q = getPrime(bit_size // 2)
        n = p * q
        phi = (p-1) * (q-1)
        # test if phi and e are coprime
        if gcd(e, phi) == 1:
            break
    return n, e

def encrypt_message(plaintext, key):
    n, e = key
    encoded = bytes_to_long(bytes(plaintext, "utf-8"))
    ciphertext = pow(encoded, e, n)
    return {"message": f"{ciphertext:X}", "public_key": [f"{n:X}", f"{e:X}"]}

def get_secret():
    public_key = get_new_public_key(bit_size, e)
    
    return encrypt_message(super_secret_message, public_key)

if __name__=="__main__":
    print(get_secret())