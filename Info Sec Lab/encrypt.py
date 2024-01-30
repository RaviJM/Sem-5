# encrypt.py
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Load the recipient's public key from a file
with open("D:\\COLLEGE\\Information Security Lab\\Project\\public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())

# Read the file to be encrypted
with open("D:\\COLLEGE\\Information Security Lab\\Project\\file.txt", "rb") as file:
    data_to_encrypt = file.read()

# Encrypt the data using the recipient's public key
encrypted_data = public_key.encrypt(
    data_to_encrypt,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save the encrypted data to a file
with open("D:\\COLLEGE\\Information Security Lab\\Project\\encrypted_file.txt", "wb") as file:
    file.write(encrypted_data)
