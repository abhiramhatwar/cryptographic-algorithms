import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2, x1 = x1, x
        d, y1 = y1, y
    if temp_phi == 1:
        return d + phi

def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

p = 61
q = 53
public, private = generate_keypair(p, q)
plaintext = "HELLO"
ciphertext = encrypt(public, plaintext)
decrypted_text = decrypt(private, ciphertext)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
