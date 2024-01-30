import streamlit as st
import base64
import random


# Function to compute the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute the modular inverse
def mod_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = y2 - temp1 * y1

        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if temp_phi == 1:
        d = y2 + phi

    return d

# Function to perform RSA encryption
def rsa_encrypt(plaintext, e, n):
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

# Read the content of the file to be encrypted
def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data

# Write the encrypted data to a file
def write_encrypted_file(encrypted_data, file_name):
    with open(file_name, 'w') as file:
        file.write(' '.join(map(str, encrypted_data)))

# Function to perform RSA decryption
def rsa_decrypt(ciphertext, d, n):
    decrypted_text = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted_text)

# Read the encrypted data from a file
def read_encrypted_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read().split()
    return [int(c) for c in data]

# Write the decrypted data to a file
def write_decrypted_file(decrypted_data, file_name):
    with open(file_name, 'w') as file:
        file.write(decrypted_data)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def generate_e(p, q):
    phi = (p - 1) * (q - 1)

    # Finding a random prime number 'e' that is relatively prime to phi
    while True:
        e = random.randint(2, phi - 1)  # Random number between 2 and phi - 1
        if gcd(e, phi) == 1:
            return e

def main():
    st.title('File Encryption and Decryption using RSA')

    mode = st.radio("Choose mode:", ("Encryption", "Decryption"))

    if mode == "Encryption":
        p_input = st.text_input("Enter first prime number to generate the public key and encrypt")
        q_input = st.text_input("Enter second prime number to generate the public key and encrypt")

        if p_input and q_input:
            p = int(p_input)
            q = int(q_input)
            if not is_prime(p) or not is_prime(q):
                st.error("Please enter prime numbers!")
            else:
                e = generate_e(p, q)
                d_output = mod_inverse(e, (p - 1) * (q - 1))
                n_output = p * q

                uploaded_file = st.file_uploader("Upload a file to Encrypt", type=["txt"])
                if uploaded_file is not None:
                    try:
                        file_contents = uploaded_file.read().decode("utf-8")
                        encrypted_data = rsa_encrypt(file_contents, e, n_output)
                        write_encrypted_file(encrypted_data, "encrypted_data.txt")

                        st.text(f"The private key for this encryption is: {d_output}")
                        st.text(f"n for this encryption is: {n_output}")

                        st.subheader("Download Encrypted Data:")
                        st.markdown(get_binary_file_downloader_html("encrypted_data.txt", 'Download Encrypted Data'), unsafe_allow_html=True)

                    except Exception as e:
                        st.text("Error Occurred")

    else:
        d_input = st.text_input("Enter private key provided while encryption")
        n_input = st.text_input("Enter n provided while encryption")
        uploaded_file = st.file_uploader("Upload a file to Decrypt", type=["txt"])
        if uploaded_file is not None:
            try:

                file_contents = uploaded_file.read().decode("utf-8")
                encrypted_data = [int(c) for c in file_contents.split()]
                if d_input and n_input:
                    d = int(d_input)
                    n = int(n_input)
                    decrypted_data = rsa_decrypt(encrypted_data, d, n)
                    write_decrypted_file(decrypted_data, "decrypted_data.txt")
                    st.subheader("Download Decrypted Data:")
                    st.markdown(get_binary_file_downloader_html("decrypted_data.txt", 'Download Decrypted Data'), unsafe_allow_html=True)

            except Exception as e:
                st.text("Error Occurred")



def get_binary_file_downloader_html(bin_data, file_label='File'):
    data = open(bin_data, 'r').read()
    b64 = base64.b64encode(data.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{file_label}.txt">Click here to download the data</a>'
    return href

if __name__ == '__main__':
    main()
