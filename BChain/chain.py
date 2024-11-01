import hashlib
import random
from block import Block
from user import User


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.stakeholders = []  # List of all users

    # Create the first block (genesis block)
    def create_genesis_block(self):
        user0 = User("TK")
        return Block(0, "Genesis Block", "0", user=user0, validator=user0)

    # Get the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1]

    def register_user(self, user: User):
        self.stakeholders.append(user)

    def add_stake(self, user: User, amount: int):
        user.stake += amount  # Increase user's stake
        self.register_user(user)

    # Select a validator based on stake proportionally
    def select_validator(self):
        total_stake = sum(user.stake for user in self.stakeholders)
        if total_stake == 0:
            print("No user has any stake.")
            return None
        
        # Create a weighted selection based on stake
        weights = [user.stake / total_stake for user in self.stakeholders]
        selected_user = random.choices(self.stakeholders, weights=weights, k=1)[0]
        return selected_user


    # Add a new block to the chain
    def add_block(self, data, user: User):
        # previous_block = self.get_latest_block()
        # if new_block.verify_signature():
        #     self.chain.append(new_block)
        validator = self.select_validator()
        if validator:
            previous_block = self.get_latest_block()
            # new_block = Block(len(self.chain), data, previous_block.hash, validator)
            new_block = Block(len(self.chain), data, previous_block.hash, user, validator)


            if new_block.verify_signature():
                self.chain.append(new_block)
                print(f"Block {new_block.block_number} added by {validator.name} (Stake: {validator.stake}).")
            else:
                print("Invalid block signature.")
        else:
            print("No valid validator available.")


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

