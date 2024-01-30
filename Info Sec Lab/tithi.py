from io import BytesIO
import streamlit as st
import os
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



# Encrypt function
def encrypt_file(password, file_data):

    plaintext = file_data.read()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32 + 16,  # key size + IV size
        salt=salt,
        iterations=10000,
        backend=default_backend()
    )
    key_iv = kdf.derive(password.encode())

    key = key_iv[:32]
    iv = key_iv[32:]

    # Convert the file_data (BytesIO) into a bytes object
    plaintext = file_data.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(plaintext) + encryptor.finalize()

    # Add 'Salted__' magic bytes and prepend salt
    result = b'Salted__' + salt + encrypted_text

    return result

# Decrypt function (modify as needed)
def decrypt_file(password, file_data):
    salt = file_data[8:24]
    ciphertext = file_data[24:]

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32 + 16,
        salt=salt,
        iterations=10000,
        backend=default_backend()
    )
    key_iv = kdf.derive(password.encode())

    key = key_iv[:32]
    iv = key_iv[32:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_text

st.title("File Encryption and Decryption")

uploaded_file = st.file_uploader("Upload a file for encryption/decryption")




if uploaded_file:
    st.write("File uploaded successfully.")
    st.write(f"Filename: {uploaded_file.name}")

    operation = st.radio("Choose operation", ("Encrypt", "Decrypt"))

    if operation == "Encrypt":
        password = st.text_input("Enter a password for encryption", type="password")
        if st.button("Encrypt"):
            if password:
                with st.spinner('Encrypting...'):
                    encrypted_content = encrypt_file(password, uploaded_file)
                st.success("File encrypted successfully. Download below.")
                st.download_button(label="Download Encrypted File", data=encrypted_content, file_name=uploaded_file.name + ".enc")
            else:
                st.error("Please enter a password.")

    elif operation == "Decrypt":
        password = st.text_input("Enter the password for decryption", type="password")
        if st.button("Decrypt"):
            if password:
                with st.spinner('Decrypting...'):
                    decrypt_file(password, uploaded_file.getvalue())
                st.success("File decrypted successfully. Download below.")
                st.download_button(label="Download Decrypted File", data=uploaded_file.getvalue(), file_name=uploaded_file.name + ".dec")
            else:
                st.error("Please enter the decryption password.")
