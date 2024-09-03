import numpy as np

def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    matrix_modulus_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_modulus_inv

def hill_cipher_encrypt(plaintext, key):
    key_matrix = np.array(key).reshape(int(len(key)**0.5), -1)
    n = key_matrix.shape[0]
    plaintext_numbers = [ord(char) - ord('A') for char in plaintext.upper()]
    if len(plaintext_numbers) % n != 0:
        plaintext_numbers += [0] * (n - len(plaintext_numbers) % n)
    plaintext_matrix = np.array(plaintext_numbers).reshape(-1, n)
    encrypted_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    ciphertext = ''.join(chr(num + ord('A')) for num in encrypted_matrix.flatten())
    return ciphertext

def hill_cipher_decrypt(ciphertext, key):
    key_matrix = np.array(key).reshape(int(len(key)**0.5), -1)
    n = key_matrix.shape[0]
    ciphertext_numbers = [ord(char) - ord('A') for char in ciphertext.upper()]
    ciphertext_matrix = np.array(ciphertext_numbers).reshape(-1, n)
    inverse_key_matrix = mod_inverse(key_matrix, 26)
    decrypted_matrix = np.dot(ciphertext_matrix, inverse_key_matrix) % 26
    plaintext = ''.join(chr(num + ord('A')) for num in decrypted_matrix.flatten())
    return plaintext

key = [6, 24, 1, 13, 16, 10, 20, 17, 15]
plaintext = "HELLO"
ciphertext = hill_cipher_encrypt(plaintext, key)
decrypted_text = hill_cipher_decrypt(ciphertext, key)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
