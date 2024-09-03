from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(24)
iv = os.urandom(8)
cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(b"Secret message") + encryptor.finalize()
