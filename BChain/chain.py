import hashlib
from block import Block
from user import User


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    # Create the first block (genesis block)
    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0", User("TK"))

    # Get the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1]

    # Add a new block to the chain
    def add_block(self, data, user: User):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), data, previous_block.hash, user)
        if new_block.verify_signature():
            self.chain.append(new_block)

    # # Tamper with a block's data
    def tamper_block(self, block_number, new_data):
        if block_number < len(self.chain):
            self.chain[block_number].data = new_data
            self.chain[block_number].hash = self.chain[block_number].calculate_hash()
            # Recalculate the hash for all subsequent blocks
            for i in range(block_number + 1, len(self.chain)):
                self.chain[i].previous_hash = self.chain[i - 1].hash
                self.chain[i].hash = self.chain[i].calculate_hash()

    # Function to print the blockchain
    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.block_number}:")
            print(f"    Data: {block.data}")
            print(f"    Hash: {block.hash}")
            print(f"    Previous Hash: {block.previous_hash}\n")


# Example: Create a blockchain and add blocks
my_blockchain = Blockchain()
user1 = User("Alice")
user2 = User("Bob")
my_blockchain.add_block(
    "First Block Data",
    user1,
)
my_blockchain.add_block("Second Block Data", user2)
my_blockchain.add_block("Third Block Data", user1)

# Print the blockchain
print("Blockchain:")
my_blockchain.print_chain()

# Tamper with the second block
my_blockchain.tamper_block(1, "Tampered Data")

print("After tampering:")
# Print the blockchain after tampering
my_blockchain.print_chain()
