# keygen.py
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# Generate an RSA key pair (public and private keys)
private_key = rsa.generate_private_key(
    public_exponent=65537,  # A common value for RSA keys
    key_size=2048,          # Adjust the key size as needed
    backend=default_backend()
)

# Save the private key to a file
with open("D:\\COLLEGE\\Information Security Lab\\Project\\private_key.pem", "wb") as key_file:
    key_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Get the public key from the private key
public_key = private_key.public_key()

# Save the public key to a file
with open("D:\\COLLEGE\\Information Security Lab\\Project\\public_key.pem", "wb") as key_file:
    key_file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )
