from pathlib import Path
from cryptography.fernet import Fernet
import sys
version = 1.0

HOME_PATH = str(Path.home())+"/"

def New(filename):
    if not filename:
        print("filename cannot be empty.")
        return

    key = Fernet.generate_key()
    key_file = Path(f"{filename}.key")

    with key_file.open("wb") as f:
        f.write(key)
    print(f"key filepath: {key_file.absolute()}")

def fetch_key():
    key_path_str = sys.argv[2]
    key_path = Path(key_path_str)
    with key_path.open("rb") as f:
        return f.read().strip()

def encrypt_file(file_path_str, key):
    try:
        fernet = Fernet(key)
        file_path = Path(file_path_str)
        with file_path.open("rb") as f:
            data = f.read()
        encrypted_data = fernet.encrypt(data)
        with file_path.open("wb") as f:
            f.write(encrypted_data)
        print("success")

    except Exception as e:
        print(f"\nfatal error: {e}")

def decrypt_file(file_path_str, key):
    try:
        fernet = Fernet(key)
        file_path = Path(file_path_str)

        with file_path.open("rb") as f:
            encrypted_data = f.read()
        decrypted_data = fernet.decrypt(encrypted_data)

        with file_path.open("wb") as f:
            f.write(decrypted_data)
        print("success")

    except Exception as e:
        print(f"\nfatal error: {e}")

def main():
    if len(sys.argv) < 2:
        print("Not enough arguments.")
        sys.exit()
    choice = sys.argv[1]

    if choice == "-k":
        New(sys.argv[2])
    
    elif choice == "-e":
        try:
            encrypt_file(sys.argv[2], sys.argv[3])
        except IndexError:
            print("Not enough arguments.")

    elif choice == "-d":
        try:
            decrypt_file(sys.argv[2], sys.argv[3])
        except IndexError:
            print("Not enough arguments.")
    
    else:
        print(f"error at {sys.argv[0]}, no option {sys.argv[1]}")
if __name__ == "__main__":
    main()
