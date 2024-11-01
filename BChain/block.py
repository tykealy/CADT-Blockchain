from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import hashlib

from user import User


import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Block:
    def __init__(self, block_number, data, previous_hash, user, validator):
        self.block_number = block_number
        self.data = data
        self.previous_hash = previous_hash
        self.validator = validator
        self.hash = self.calculate_hash()
        self.signature = user.sign_data(self.hash)
        self.public_key_pem = user.get_public_key_pem()

    def calculate_hash(self):
        block_contents = str(self.block_number) + self.data + self.previous_hash
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def verify_signature(self):
        try:
            public_key = serialization.load_pem_public_key(self.public_key_pem.encode())
            calculated_hash = self.calculate_hash().encode()
            public_key.verify(
                self.signature,
                calculated_hash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )
            return True
        except Exception as e:
            return False


# # Create a user and generate RSA key pair
# alice = User("Alice")

# # Data to be included in the block
# data = "First Block Data"
# previous_hash = "0"  # 0 is the previous hash for genesis block

# # Create a block and print its hash
# block = Block(1, data, previous_hash, alice)
# print(f"Block 1 Hash: {block.hash}")

# # Verify the signature
# if block.verify_signature():
#     print("Signature is valid.")
# else:
#     print("Signature verification failed.")
