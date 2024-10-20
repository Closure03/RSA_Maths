from Cryptodome.PublicKey import RSA

# Generate both keys
key = RSA.generate(2048)

# storing the private key
with open("priv.pem", "wb") as f:
    f.write(key.export_key('PEM'))

# storing the public key
with open("pub.pem", "wb") as f:
    f.write(key.publickey().export_key('PEM'))