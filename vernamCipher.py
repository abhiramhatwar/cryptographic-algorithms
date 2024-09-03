def vernam_encrypt(plaintext, key):
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext

def vernam_decrypt(ciphertext, key):
    plaintext = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))
    return plaintext

plaintext = "HELLO"
key = "XMCKL"
ciphertext = vernam_encrypt(plaintext, key)
decrypted_text = vernam_decrypt(ciphertext, key)

print(f"Ciphertext: {''.join(format(ord(c), '02x') for c in ciphertext)}")
print(f"Decrypted Text: {decrypted_text}")
