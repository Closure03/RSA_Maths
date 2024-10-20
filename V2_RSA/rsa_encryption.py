from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Generación de claves RSA
def generar_claves():
    # Genera un par de claves (privada y pública)
    
    key = RSA.generate(2048)
    
    # Clave privada
    clave_privada = key.export_key()
    with open("clave_privada.txt", "wb") as f:
        f.write(clave_privada)
    
    # Clave pública
    clave_publica = key.publickey().export_key()
    with open("clave_publica.txt", "wb") as f:
        f.write(clave_publica)

# Función para encriptar un mensaje usando la clave pública
def encriptar_mensaje(mensaje):
    with open("clave_publica.txt", "rb") as f:
        clave_publica = RSA.import_key(f.read())
    
    # Crear el objeto de cifrado
    cifrador = PKCS1_OAEP.new(clave_publica)
    
    # Cifrar el mensaje
    mensaje_encriptado = cifrador.encrypt(mensaje)
    
    with open("mensaje_encriptado.txt", "wb") as f:
        f.write(mensaje_encriptado)
    
    return mensaje_encriptado

# Función para desencriptar un mensaje usando la clave privada
def desencriptar_mensaje():
    with open("clave_privada.txt", "rb") as f:
        clave_privada = RSA.import_key(f.read())
    
    # Crear el objeto de descifrado
    descifrador = PKCS1_OAEP.new(clave_privada)
    
    with open("mensaje_encriptado.txt", "rb") as f:
        mensaje_encriptado = f.read()
    
    # Desencriptar el mensaje
    mensaje_desencriptado = descifrador.decrypt(mensaje_encriptado)
    
    return mensaje_desencriptado

# Ejecución del código
if __name__ == "__main__":
    # Generar las claves y guardarlas en archivos
    generar_claves()
    
    # Mensaje de ejemplo
    mensaje = b"Este es un mensaje secreto."
    
    # Encriptar el mensaje
    print("Encriptando mensaje...")
    encriptado = encriptar_mensaje(mensaje)
    print("Mensaje encriptado guardado en mensaje_encriptado.txt")
    
    # Desencriptar el mensaje
    print("Desencriptando mensaje...")
    desencriptado = desencriptar_mensaje()
    print("Mensaje desencriptado:", desencriptado.decode())
