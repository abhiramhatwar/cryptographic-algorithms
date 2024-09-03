from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()
message = b"Secret message"
signature = private_key.sign(message, hashes.SHA256())
