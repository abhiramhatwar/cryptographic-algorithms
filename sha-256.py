import hashlib

def sha256_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

message = "Hello, World!"
hash_value = sha256_hash(message)

print(f"Message: {message}")
print(f"SHA-256 Hash: {hash_value}")
