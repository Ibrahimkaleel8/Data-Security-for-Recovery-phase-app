from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
import codecs

# Generating private keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Generating public keys
public_key = private_key.public_key()


def algo2_encrypt():
    ciphertext = public_key.encrypt(
        text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    print(ciphertext)
    return ciphertext


def algo2_decrypt(ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    result = codecs.decode(plaintext)
    print(result)


if __name__ == "__main__":
    str_input = input("Enter recovery phase: ")
    text = str_input.encode('utf-8')
    ciphertext = algo2_encrypt()
    algo2_decrypt(ciphertext)
