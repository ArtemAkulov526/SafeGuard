from cryptography.fernet import Fernet

def encrypt_file(file):
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    with open(file, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(file, "wb") as f:
        f.write(encrypted)


if __name__ == "__main__":

    encrypt_file("file.txt")

