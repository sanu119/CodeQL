from Crypto.Cipher import AES
import hashlib

# 🚫 Hardcoded secret key
SECRET_KEY = 'my_weak_secret'  # CodeQL will detect this as hardcoded secret

# 🚫 Weak hash function (MD5)
def get_md5_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

# 🚫 Using ECB mode (Electronic Codebook)
def encrypt_message(message):
    key = SECRET_KEY.ljust(16)[:16].encode()  # force to 16 bytes
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = message + ' ' * (16 - len(message) % 16)  # naive padding
    encrypted = cipher.encrypt(padded_message.encode())
    return encrypted

def decrypt_message(encrypted):
    key = SECRET_KEY.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted).decode().strip()
    return decrypted

if __name__ == "__main__":
    message = "SensitiveData123"
    
    # Hashing (bad practice: MD5)
    print("MD5 Hash:", get_md5_hash(message))

    # Encryption (bad practice: ECB mode, hardcoded key)
    encrypted = encrypt_message(message)
    print("Encrypted:", encrypted)

    decrypted = decrypt_message(encrypted)
    print("Decrypted:", decrypted)
