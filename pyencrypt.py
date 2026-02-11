from pathlib import Path
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from cryptography.fernet import Fernet

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
    key_path_str = inquirer.filepath(
        message="select .key file:",
        default=HOME_PATH,
        validate=PathValidator(is_file=True, message="invalid filepath"),
        only_files=True,
    ).execute()

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
    print(f"pyencrypt v{version}")
    while True:
        choice = inquirer.rawlist(
            message="Select an option: ",
            choices=["Generate key", "Encrypt file", "Decrypt file", "View License", "Exit"],
        ).execute()

        if choice == "View License":
            print('''\n
    This work is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/
''')
        
        if choice == "Exit":
            break

        if choice == "Generate key":
            name = inquirer.text(message="Enter filename for the key (no extension):").execute()
            New(name)

        elif choice in ["Encrypt file", "Decrypt file"]:
            target_file = inquirer.filepath(
                message=f"Select file to {choice.split()[0].lower()}:",
                default=HOME_PATH,
                validate=PathValidator(is_file=True, message="Must select a file"),
                only_files=True,
            ).execute()
            try:
                key = fetch_key()

                if choice == "Encrypt file":
                    encrypt_file(target_file, key)
                else:
                    decrypt_file(target_file, key)
            except Exception as e:
                print(f"\nerror loading key: {e}")

if __name__ == "__main__":
    main()
