import random

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primitive_root(p):
    if not is_prime(p):
        raise ValueError("p must be a prime number")
    if p == 2:
        return 1

    phi = p - 1
    factors = set()
    n = phi
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)

    for g in range(2, p):
        if all(pow(g, phi // factor, p) != 1 for factor in factors):
            return g

    raise ValueError("No primitive root found")

def diffie_hellman(p, g):
    a = random.randint(2, p-2)
    b = random.randint(2, p-2)
    
    A = pow(g, a, p)
    B = pow(g, b, p)

    s_a = pow(B, a, p)
    s_b = pow(A, b, p)

    return A, B, s_a, s_b

p = 23
g = find_primitive_root(p)
A, B, s_a, s_b = diffie_hellman(p, g)

print(f"Prime (p): {p}")
print(f"Primitive root (g): {g}")
print(f"Public value A (g^a mod p): {A}")
print(f"Public value B (g^b mod p): {B}")
print(f"Shared secret calculated by A: {s_a}")
print(f"Shared secret calculated by B: {s_b}")
