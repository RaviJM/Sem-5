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





# Sample file to encrypt
folder = "D:\\COLLEGE\\Information Security Lab\\Project\\"
file_name = folder + "file.txt"




# Sample text to encrypt
plaintext = read_file(file_name)

# Generate prime numbers 'p' and 'q' (normally large prime numbers in practice)
p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 65537  # Public exponent (commonly used)
d = mod_inverse(e, phi)  # Private exponent

# Encrypt the file content
encrypted_data = rsa_encrypt(plaintext, e, n)

# Write the encrypted data to a new file
write_encrypted_file(encrypted_data, folder + "encrypted_file.txt")




encrypted_file_name = folder + "encrypted_file.txt"

# Read the encrypted data
encrypted_data = read_encrypted_file(encrypted_file_name)

# Decrypt the data
decrypted_data = rsa_decrypt(encrypted_data, d, n)

# File name to save the decrypted data
decrypted_file_name = folder + "decrypted_file.txt"

# Write the decrypted data to a new file
write_decrypted_file(decrypted_data, decrypted_file_name)
