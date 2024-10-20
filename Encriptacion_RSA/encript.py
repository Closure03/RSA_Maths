from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

line = bytes("hola caracola", encoding="utf8")

try:
    with open("pub.pem", "rb") as f:
        public_key = f.read()  # Reading the key from the file
        public_key = RSA.import_key(public_key)  # Importing the key
        RSA_encryptor = PKCS1_OAEP.new(public_key)  # Creating an encryptor with the loaded key
        encrypted_line = RSA_encryptor.encrypt(line)  # Encrypting
except IOError:
    print("ERROR")
except:
    encrypted_line = None

print(encrypted_line)

with open("example.bin", "wb") as f:
    f.write(encrypted_line)