from user import User
from chain import  Blockchain

# Example: Create a blockchain and add blocks
my_blockchain = Blockchain()

# Create a list of User instances
users = [
    User("Alice"),
    User("Bob"),
    User("Charlie"),
    User("David"),
    User("Eve"),
    User("Frank"),
    User("Grace"),
    User("Hank"),
    User("Ivy"),
    User("Judy")
]

# Example usage
for user in users:
    my_blockchain.add_stake(user, 10)


my_blockchain.add_block("Candidate A", users[0])
my_blockchain.add_block("Candidate B", users[1])
my_blockchain.add_block("Candidate A", users[2])
my_blockchain.add_block("Candidate A", users[3])
my_blockchain.add_block("Candidate B", users[4])
my_blockchain.add_block("Candidate A", users[5])


# my_blockchain.add_block(
#     "First Block Data",
#     user1,
# )
# my_blockchain.add_block("Second Block Data", user2)
# my_blockchain.add_block("Third Block Data", user1)

#Print the blockchain
print("Blockchain:")
my_blockchain.print_chain()

# # Tamper with the second block
# my_blockchain.tamper_block(1, "Tampered Data")

# print("After tampering:")
# # Print the blockchain after tampering
# my_blockchain.print_chain()