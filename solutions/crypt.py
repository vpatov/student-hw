from cryptography.fernet import Fernet
import sys

def decrypt_file(source_filename, destination_filename, fernet: Fernet):
    with open(source_filename, 'rb') as f:
        encrypted = f.read()

    with open(destination_filename, 'wb') as f:
        decrypted = fernet.decrypt(encrypted)
        f.write(decrypted)


def load_fernet_key(key_file_name):
    with open(key_file_name, 'rb') as filekey:
        return Fernet(filekey.read())

def encrypt_file(source_filename, destination_filename, fernet):
    with open(source_filename, 'rb') as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(destination_filename, 'wb') as f:
        f.write(encrypted)


if len(sys.argv) < 5:
    raise Exception(
        "Not enough arguments.\n"
        "Usage: python3 ./crypt.py <encrypt|decrypt> <path_to_key_file> "
        "<source_filename> <destination_filename>"
    )

mode = sys.argv[1]

if mode not in ['encrypt','decrypt']:
    raise Exception("mode must be either encrypt or decrypt")

key_file = sys.argv[2]
source_file = sys.argv[3]
destination_file = sys.argv[4]

if key_file.endswith('py'):
    raise Exception("The second argument should be the key file, "
                    "not the python script. Be careful when using this program, "
                    "because it could overwrite your files.")

fernet = load_fernet_key(key_file)
if mode == 'encrypt':
    encrypt_file(source_file, destination_file + '.encrypted', fernet)

elif mode == 'decrypt':
    decrypt_file(source_file, destination_file + '.decrypted', fernet)