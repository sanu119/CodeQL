from cryptography.fernet import Fernet

# Generate and save a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt a message
def encrypt_message(message: str, key: bytes) -> bytes:
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

# Decrypt a message
def decrypt_message(encrypted_message: bytes, key: bytes) -> str:
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message)
    return decrypted.decode()

if __name__ == "__main__":
    generate_key()
    key = load_key()

    original_message = "TopSecret123"
    encrypted = encrypt_message(original_message, key)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt_message(encrypted, key)
    print(f"Decrypted: {decrypted}")
