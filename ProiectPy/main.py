
import hashlib
import sys

def encrypt_file(input_file, password):
    with open(input_file, 'rb') as file:
        data = file.read()

    encrypted_data = bytearray()

    for i, byte in enumerate(data):
        password_byte = ord(password[i % len(password)])
        encrypted_byte = (byte + password_byte) % 256
        encrypted_data.append(encrypted_byte)

    output_file = input_file + '.crypted'

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

    # genram hash-ul fisierului original
    original_file_hash = hashlib.sha256(data).hexdigest()
    with open(output_file + '.hash', 'w') as hash_file:
        hash_file.write(original_file_hash)


def decrypt_file(input_file, password):
    with open(input_file, 'rb') as file:
        data = file.read()

    decrypted_data = bytearray()

    for i, byte in enumerate(data):
        password_byte = ord(password[i % len(password)])
        decrypted_byte = (byte - password_byte) % 256
        decrypted_data.append(decrypted_byte)



    # Verificam daca parola este corecta
    with open(input_file + '.hash', 'r') as hash_file:
        original_file_hash = hash_file.read()

    decrypted_file_hash = hashlib.sha256(decrypted_data).hexdigest()

    if decrypted_file_hash == original_file_hash:
        output_file = input_file.replace('.crypted', '') + '.decrypted'

        with open(output_file, 'wb') as file:
            file.write(decrypted_data)
        print("Decryption successful. Password is correct.")
    else:
        print("Decryption failed. Incorrect password.")
        sys.exit(1)


def main():
    if len(sys.argv) < 4:
        print("Usage: main.py [crypt/decrypt] [input_file] [password]")
        sys.exit(1)

    command = sys.argv[1]
    input_file = sys.argv[2]
    password = sys.argv[3]

    if command == 'crypt':
        encrypt_file(input_file, password)
        print(f"File {input_file} encrypted successfully.")
    elif command == 'decrypt':
        decrypt_file(input_file, password)
    else:
        print("Invalid command. Use 'crypt' or 'decrypt.")


if __name__ == "__main__":
    main()
