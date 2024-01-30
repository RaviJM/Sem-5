# decrypt.py
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

# Load the private key from a file
with open("D:\\COLLEGE\\Information Security Lab\\Project\\private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())

# Read the encrypted file
with open("D:\\COLLEGE\\Information Security Lab\\Project\\encrypted_file.txt", "rb") as file:
    encrypted_data = file.read()

# Decrypt the data using RSA private key
decrypted_data = private_key.decrypt(
    encrypted_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Save the decrypted data to a file
with open("D:\\COLLEGE\\Information Security Lab\\Project\\decrypted_file.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("Decryption completed. Decrypted data saved to decrypted_file.txt.")
