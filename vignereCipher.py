def generate_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return ''.join(key)
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def vignere_encrypt(plaintext, key):
    key = generate_key(plaintext, key)
    ciphertext = ''.join(
        chr((ord(p) + ord(k)) % 26 + ord('A'))
        for p, k in zip(plaintext.upper(), key.upper())
    )
    return ciphertext

def vignere_decrypt(ciphertext, key):
    key = generate_key(ciphertext, key)
    plaintext = ''.join(
        chr((ord(c) - ord(k) + 26) % 26 + ord('A'))
        for c, k in zip(ciphertext.upper(), key.upper())
    )
    return plaintext

plaintext = "HELLO"
key = "KEY"
ciphertext = vignere_encrypt(plaintext, key)
decrypted_text = vignere_decrypt(ciphertext, key)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
