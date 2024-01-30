def encrypt(message, key):  # To encrypt the message using encrypt function
    msg = ""
    for i in message:
        if i.isalpha():
            if i.isupper(): # If letter is in Upper Case
                alphabet = ord(i) - ord('A')  # To convert the ascii values in the range of 1-26
                encrypted_alphabet = (alphabet + key) % 26 # Shift the value by using the given key
                encrypted_char = chr(encrypted_alphabet + ord('A'))  # Again convert it to the ascii
                msg += encrypted_char # Append the encypted character into msg string
            else: # If letter is in lower case
                alphabet = ord(i) - ord('a')  # To convert the ascii values in the range og 1-26
                encrypted_alphabet = (alphabet + key) % 26 # Shift the value by using the given key
                encrypted_char = chr(encrypted_alphabet + ord('a'))  # Again convert it to the ascii
                msg += encrypted_char # Append the encypted character into msg string
        else:
            msg += i # If it is not alphabet then append it as it is 
    return msg

def decrypt(message, key): # To decrypt the encrypted message, we will perform reverse method
    msg1 = ""
    for i in message:
        if i.isalpha(): # If it is alphabet
            if i.isupper(): # for upper case letter
                alphabet = ord(i) - ord('A') # To convert it in the range of 1-26
                decrypted_alphabet = (alphabet - key) % 26 # Subtract the key from the alphabet's number in the range of 1-26
                decrypted_char = chr(decrypted_alphabet + ord('A'))  # again convert it to ascii
                msg1 += decrypted_char # append the decrypted message in to empty string
            else: # Lower case
                alphabet = ord(i) - ord('a') # To convert it in the range of 1-26
                decrypted_alphabet = (alphabet - key) % 26 # Subtract the key from the alphabet's number in the range of 1-26
                decrypted_char = chr(decrypted_alphabet + ord('a'))  # again convert it to ascii
                msg1 += decrypted_char # append the decrypted message in to empty string
        else:
            msg1 += i 
        
    return msg1

# Performing Cryptanalysis
# Without the key we can decrypt the data
def decrypt_2(message):
    for key in range(26):
        decrypted_msg = decrypt(message, key)
        print(f"Key: {key}, Decrypted Message: {decrypted_msg}")

message = str(input("Enter a message: "))
key = int(input("Enter key: "))
# chr used to convert from ascii to alphabet
# ord used to convert from alphabet to ascii
msge = encrypt(message, key)
print("Encrypted msg = ", msge)

decrypt_2(msge)