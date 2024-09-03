from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()
message = b"Secret message"
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
