import streamlit as st

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

# function to check if a number is prime or not
def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


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





# # Sample file to encrypt
# folder = "D:\\COLLEGE\\Information Security Lab\\Project\\"
# file_name = folder + "file.txt"
#
# # Sample text to encrypt
# plaintext = read_file(file_name)
#


###############################################################################

# # Encrypt the file content
# encrypted_data = rsa_encrypt(plaintext, e, n)
#
# # Write the encrypted data to a new file
# write_encrypted_file(encrypted_data, folder + "encrypted_file.txt")




# encrypted_file_name = folder + "encrypted_file.txt"







# # Read the encrypted data
# encrypted_data = read_encrypted_file(encrypted_file_name)
#
# # Decrypt the data
# decrypted_data = rsa_decrypt(encrypted_data, d, n)
#
# # File name to save the decrypted data
# decrypted_file_name = folder + "decrypted_file.txt"
#
# # Write the decrypted data to a new file
# write_decrypted_file(decrypted_data, decrypted_file_name)
#
#




# Define the Streamlit app
# st.title("RSA Encryption and Decryption")
st.set_page_config(page_title="RSA Encryption and Decryption", layout="wide")

# Create radio buttons to choose encryption or decryption
mode = st.radio("Choose Mode:", ("Encryption", "Decryption"))

if mode == "Encryption":

    st.subheader("Encryption Mode")
    uploaded_file = st.file_uploader("Upload a .txt file for encryption", type=["txt"])

    if uploaded_file:
        p = st.number_input("Enter 'p' value:", step=1, value=0, min_value=None, max_value=None)
        q = st.number_input("Enter 'q' value:", step=1, value=0, min_value=None, max_value=None)


        if st.button("Encrypt"):
            if isPrime(p) and isPrime(q):
                # Generate prime numbers 'p' and 'q' (normally large prime numbers in practice)
                # p = 61
                # q = 53

                n = p * q
                phi = (p - 1) * (q - 1)

                e = 65537  # Public exponent (commonly used)
                d = mod_inverse(e, phi)  # Private exponent

                # Encrypt the uploaded file
                # encrypted_text = encrypt(uploaded_file, n)

                # Encrypt the file content
                plaintext = uploaded_file.read()
                plaintext = str(plaintext)
                # plaintext = read_file(uploaded_file)
                encrypted_data = rsa_encrypt(plaintext, e, n)
                str1 = ""
                for obj in encrypted_data:
                    str1 += obj
                    str1 += " "
                # encrypted_data = str(encrypted_data)



                # Write the encrypted data to a file
                # with open("encrypted_file.txt", "w") as encrypted_file:
                #     encrypted_file.write(' '.join(map(str, encrypted_data)))

                # Display and offer download of the encrypted file
                st.write("Encrypted File:")

                st.download_button("Download Encrypted File", data=str1, key="encrypted_file.txt")

                # Display 'n' and 'd' for the user to note
                st.write(f"Value of 'n': {n}")
                st.write(f"Value of 'd': {d}")

                # # Display and offer download of the encrypted file
                # st.write("Encrypted File:")
                # st.write(encrypted_text)
                # st.download_button("Download Encrypted File", data=encrypted_text, key="encrypted_file.txt")
                #
                # # Display 'n' and 'd' for user to note
                # st.write(f"Value of 'n': {n}")
                # st.write(f"Value of 'd': {d}")

elif mode == "Decryption":
    st.subheader("Decryption Mode")
    encrypted_file = st.file_uploader("Upload the encrypted file (encrypted_file.txt)")
    d = st.number_input("Enter 'd' value:", step=1, value=0, min_value=None, max_value=None)
    n = st.number_input("Enter 'n' value:", step=1, value=0, min_value=None, max_value=None)

    if st.button("Decrypt"):

        if encrypted_file:
            # Read the encrypted data from the uploaded file
            # encrypted_data = read_encrypted_file(encrypted_file)
            encrypted_data = encrypted_file.read()

            # Decrypt the uploaded data
            decrypted_text = rsa_decrypt(encrypted_data, d, n)

            # # Write the decrypted data to a file
            # with open("decrypted_file.txt", "w") as decrypted_file:
            #     decrypted_file.write(decrypted_text)

            # Display and offer download of the decrypted file
            st.write("Decrypted File:")
            st.download_button("Download Decrypted File", data=decrypted_text, key="decrypted_file.txt")

        # # Decrypt the uploaded file
        # decrypted_text = decrypt(encrypted_file, d, n)
        #
        # # Display and offer download of the decrypted file
        # st.write("Decrypted File:")
        # st.write(decrypted_text)
        # st.download_button("Download Decrypted File", data=decrypted_text, key="decrypted_file.txt")


# # Run the Streamlit app
# if __name__ == '__main__':
#
#     st.write("Note: This is a basic example. Make sure to integrate your RSA encryption and decryption functions into the code.")
