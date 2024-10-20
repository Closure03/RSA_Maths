from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

try:
    with open("priv.pem","rb" as ) as f:
        priv_key = f.read() # read private key
        priv_key = RSA.import_key(priv_key) # import private key
    RSA_encryptor = PKCS1_OAEP.new(priv_key) #creating a new RSA encryption

    with open("example.bin", "rb") as f:
        line = f.read() # reading the encrypted file

    text = RSA.encryptor.decrypt(line) #Decrypting the file
except IOError:
    print("Error")
except:
    text = None

print(str(text, encoding='utf-8'))
