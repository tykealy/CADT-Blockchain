# Create a user and generate RSA key pair
alice = User("Alice")

# Data to be included in the block
data = "First Block Data"
previous_hash = "0"  # 0 is the previous hash for genesis block

# Sign the data
signature = alice.sign_data(data)

# Serialize the public key to PEM format
public_key_pem = alice.get_public_key_pem()

# Create a block and print its hash
block = Block(1, data, previous_hash, signature, public_key_pem)
print(f"Block 1 Hash: {block.hash}")

# Verify the signature
if block.verify_signature():
    print("Signature is valid.")
else:
    print("Signature verification failed.")