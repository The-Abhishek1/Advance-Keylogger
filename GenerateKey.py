from cryptography.fernet import Fernet

#Generating a key for encryption and decryption
key = Fernet.generate_key()
file = open("encryption_key.txt", "wb")
file.write(key)
file.close()