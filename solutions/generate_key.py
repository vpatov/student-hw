from cryptography.fernet import Fernet
import sys

key_filename = sys.argv[1]

with open(key_filename, 'wb') as filekey:
   filekey.write(Fernet.generate_key())



