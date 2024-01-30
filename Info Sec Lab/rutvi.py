import streamlit as st
from cryptography.fernet import Fernet
import base64

st.set_page_config(
    page_title="Web Browser Based File Encryption / Decryption",
    page_icon="🔒",
    layout="wide"
)

st.markdown("<h1>Web Browser Based File Encryption / Decryption</h1>", unsafe_allow_html=True)
st.markdown("Use your web browser to encrypt and decrypt files.")
st.markdown("<hr>", unsafe_allow_html=True)

mode = st.radio("Select Mode:", ["Encrypt", "Decrypt"])

if mode == "Encrypt":
    st.markdown("<h2>Encrypt a File</h2>")
    st.markdown("To encrypt a file, enter a password and select the file to be encrypted.")
    password = st.text_input("Password", type="password")
    file_to_encrypt = st.file_uploader("Upload File to Encrypt")

    if st.button("Encrypt File"):
        if password and file_to_encrypt:
            # Perform encryption here
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            encrypted_file = cipher_suite.encrypt(file_to_encrypt.read())
            st.success("File encrypted successfully!")

            # Save the encrypted file and key
            st.download_button(
                label="Download Encrypted File",
                data=base64.b64encode(encrypted_file).decode(),
                key="encrypted_file.txt",
            )
            # Save the encryption key
            with open("encryption_key.key", "wb") as key_file:
                key_file.write(key)

if mode == "Decrypt":
    st.markdown("<h2>Decrypt a File</h2>")
    st.markdown("Decrypt a file using the password that was previously used for encryption.")
    password_decrypt = st.text_input("Password (used for encryption)", type="password")
    file_to_decrypt = st.file_uploader("Upload File to Decrypt")

    if st.button("Decrypt File"):
        if password_decrypt and file_to_decrypt:
            try:
                # Load the encryption key from the saved file
                with open("encryption_key.key", "rb") as key_file:
                    key = key_file.read()

                cipher_suite = Fernet(key)
                decrypted_file = cipher_suite.decrypt(file_to_decrypt.read())
                st.success("File decrypted successfully!")

                # Save the decrypted file
                st.download_button(
                    label="Download Decrypted File",
                    data=base64.b64encode(decrypted_file).decode(),
                    key="decrypted_file.txt",
                )

            except Exception as e:
                st.error(f"Decryption error: {str(e)}")
        else:
            st.warning("Please enter the correct password and select a file to decrypt.")