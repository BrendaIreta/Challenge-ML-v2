import secrets

# Generar una clave secreta de 32 bytes (256 bits)
secret_key = secrets.token_hex(32)
print(secret_key)
