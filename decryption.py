from cryptography.fernet import Fernet

def decrypt_file(file):
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    with open(file, "rb") as f:
        encrypted_data = f.read()

    decrypted = fernet.decrypt(encrypted_data)

    with open(file, "wb") as f:
        f.write(decrypted)


if __name__ == "__main__":

    decrypt_file("file.txt")