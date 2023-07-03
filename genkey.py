from cryptography.fernet import Fernet

# Generar una nueva clave de encriptación
key = Fernet.generate_key()

# Imprimir la clave generada
print("Clave de encriptación generada:", key)

# Utilizar la clave generada en tu código
cipher_suite = Fernet(key)
