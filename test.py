from cryptography import fernet
import os

def encrypt(file, key):
    with open(f"{file}", "rb") as item:
        f = fernet.Fernet(key)
        file_data = item.read() 
        encrypted_data = f.encrypt(file_data)

    with open(f"{file}", "wb") as item:
        item.write(encrypted_data)
    # Adds .enc extension to encrypted file
    
        
def decrypt(file, key):
    # Decrypts the data. Gives error if you give it a different key to the one the data was encrypted with.
    with open(f"{file}", "rb") as item:
        f = fernet.Fernet(key)
        encrypted_data = item.read()
        decrypted_data = f.decrypt(encrypted_data)
    with open(f"{file}", "wb") as item:
        # Writes the decrypted data to file
        item.write(decrypted_data)


def cat(file):
    # Does the same as the cat command in Linux
    with open(f"{file}", "rt") as file:
         print(file.read())

def key_gen():
    # Decodes the key byte and appends string to a file named keys.txt
    key = fernet.Fernet.generate_key()
    # If it can't find a keys.txt file it creates a new one
    with open("keys.txt", "a") as keys:
        decoded_key = key.decode("utf-8")
        keys.write(f"{decoded_key}\n")
    keys.close()

def check_for_encryption(file):
    return file.endswith(".enc")

key = b'KNKjfQQof6MYrL9SGwV9dFDf9Gquw4VrzrE3G7ljoDk='
encrypt_test = "crypted.txt"

decrypt(encrypt_test, key)
