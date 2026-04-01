import base64
from cryptography.fernet import Fernet
import hashlib

def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encode_message(message, password):
    key = generate_key(password)
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted.decode()

def decode_message(encrypted_message, password):
    try:
        key = generate_key(password)
        cipher = Fernet(key)
        decrypted = cipher.decrypt(encrypted_message.encode())
        return decrypted.decode()
    except:
        return "Invalid key or corrupted message"
    
def save_to_file(data, filename="encrypted.txt"):
    with open(filename, "w") as f:
        f.write(data)

def load_from_file(filename="encrypted.txt"):
    try:
        with open(filename, "r") as f:
            return f.read()
    except:
        return "No file found"