import hashlib
import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, current_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = current_hash

    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, data):
        value = str(index) + previous_hash + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", str(datetime.datetime.now()), "Genesis Block", Block.calculate_hash(0, "0", str(datetime.datetime.now()), "Genesis Block"))

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        new_timestamp = str(datetime.datetime.now())
        new_hash = Block.calculate_hash(new_index, previous_block.hash, new_timestamp, data)
        new_block = Block(new_index, previous_block.hash, new_timestamp, data, new_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != Block.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

def add_transaction():
    drug_name = input("Enter the drug name: ")
    manufacturer = input("Enter the manufacturer's name: ")
    quantity = input("Enter the quantity: ")
    destination = input("Enter the destination: ")

    data = {
        'Drug Name': drug_name,
        'Manufacturer': manufacturer,
        'Quantity': quantity,
        'Destination': destination
    }
    blockchain.add_block(data)
    print("Transaction added to the blockchain.")

def view_chain():
    for block in blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}\n")

def validate_chain():
    if blockchain.is_chain_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")

def show_help():
    print("\nCommands:")
    print("1. add - Add a new transaction to the blockchain.")
    print("2. view - View the entire blockchain.")
    print("3. validate - Validate the integrity of the blockchain.")
    print("4. help - Show this help message.")
    print("5. exit - Exit the program.\n")

# Main Program Loop
blockchain = Blockchain()
print("Welcome to the Pharmaceutical Supply Chain Management System.")
show_help()

while True:
    command = input("Enter a command (type 'help' for a list of commands): ").strip().lower()

    if command == "add":
        add_transaction()
    elif command == "view":
        view_chain()
    elif command == "validate":
        validate_chain()
    elif command == "help":
        show_help()
    elif command == "exit":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid command. Please try again or type 'help' for a list of commands.")
