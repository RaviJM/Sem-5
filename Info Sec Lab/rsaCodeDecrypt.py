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

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 65537  # Public exponent (commonly used)
d = mod_inverse(e, phi)  # Private exponent


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

# File name of the encrypted file
encrypted_file_name = "D:\\COLLEGE\\Information Security Lab\\Project\\encrypted_file.txt"

# Read the encrypted data
encrypted_data = read_encrypted_file(encrypted_file_name)

# Decrypt the data
decrypted_data = rsa_decrypt(encrypted_data, d, n)

# File name to save the decrypted data
decrypted_file_name = "D:\\COLLEGE\\Information Security Lab\\Project\\decrypted_file.txt"

# Write the decrypted data to a new file
write_decrypted_file(decrypted_data, decrypted_file_name)
