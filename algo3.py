from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def algo3_encrypt(cipher, plaintext):
    # Convert plaintext to bytes
    plaintext_bytes = plaintext.encode('utf-8')
    # Pad the plaintext to a multiple of 16 bytes using PKCS#7 padding
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext_bytes) + padder.finalize()

    # Encrypt the plaintext
    encryptor = cipher.encryptor()
    ciphertext_bytes = encryptor.update(padded_plaintext) + encryptor.finalize()

    # Print the encrypted ciphertext as a hex string
    ciphertext_hex = ciphertext_bytes.hex()

    print("Encrypted ciphertext: ", ciphertext_hex)
    return ciphertext_bytes


def algo3_decrypt(cipher, ciphertext_bytes):
    # Decrypt the ciphertext
    decryptor = cipher.decryptor()
    decrypted_padded_plaintext = decryptor.update(ciphertext_bytes) + decryptor.finalize()

    # Unpad the decrypted plaintext using PKCS#7 padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_plaintext_bytes = unpadder.update(decrypted_padded_plaintext) + unpadder.finalize()

    # Print the decrypted plaintext
    decrypted_plaintext = decrypted_plaintext_bytes.decode('utf-8')
    print("Decrypted plaintext: ", decrypted_plaintext)
    return decrypted_plaintext


if __name__ == "__main__":
    # Get plaintext input from user
    plaintext = input("Enter plaintext: ")
    # Generate a random 256-bit key for AES encryption
    key = os.urandom(32)
    # Generate a random 128-bit IV for AES encryption
    iv = os.urandom(16)
    # Create an AES cipher using the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    ciphertext_bytes = algo3_encrypt(cipher, plaintext)
    decrypted_plaintext = algo3_decrypt(cipher, ciphertext_bytes)
