import hashlib
import random
import time
from cryptography.fernet import Fernet

class VotingSystem:
    def __init__(self, candidates, audit_log_file="audit_log.txt"):
        self.candidates = candidates
        self.votes = {}
        self.voter_ids = set()
        self.results = {}
        self.audit_log = []
        self.audit_log_file = audit_log_file
        self.encryption_key = Fernet.generate_key()
        self.cipher = Fernet(self.encryption_key)

    def log_event(self, event):
        """Logs events with a timestamp to the audit log."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_entry = f"{timestamp}: {event}"
        self.audit_log.append(log_entry)
        self.save_audit_log_to_file(log_entry)

    def save_audit_log_to_file(self, log_entry):
        """Saves a log entry to the audit log file."""
        with open(self.audit_log_file, "a") as file:
            file.write(log_entry + "\n")

    def generate_voter_id(self):
        """Generates a unique voter ID."""
        voter_id = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
        while voter_id in self.voter_ids:
            voter_id = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
        self.voter_ids.add(voter_id)
        self.log_event(f"Generated voter ID: {voter_id}")
        return voter_id

    def encrypt_vote(self, vote):
        """Encrypts the vote using Fernet encryption."""
        encrypted_vote = self.cipher.encrypt(vote.encode())
        return encrypted_vote

    def decrypt_vote(self, encrypted_vote):
        """Decrypts the vote using Fernet encryption."""
        decrypted_vote = self.cipher.decrypt(encrypted_vote).decode()
        return decrypted_vote

    def cast_vote(self, voter_id, candidate):
        """Casts a vote for a candidate."""
        if voter_id in self.votes:
            print("Error: Vote already cast!")
            return False
        if candidate not in self.candidates:
            print("Error: Invalid candidate!")
            return False
        
        encrypted_vote = self.encrypt_vote(candidate)
        self.votes[voter_id] = encrypted_vote
        self.log_event(f"Vote cast by voter ID: {voter_id} for candidate: {candidate}")
        print("Vote successfully cast.")
        return True

    def tally_votes(self):
        """Tallies the votes to determine the winner."""
        self.results = {candidate: 0 for candidate in self.candidates}
        for encrypted_vote in self.votes.values():
            vote = self.decrypt_vote(encrypted_vote)
            self.results[vote] += 1
        self.log_event("Votes tallied")

    def display_results(self):
        """Displays the election results."""
        print("\nElection Results:")
        for candidate, count in self.results.items():
            print(f"{candidate}: {count} votes")
        self.log_event("Results displayed")

    def display_audit_log(self):
        """Displays the audit log for verification."""
        print("\nAudit Log:")
        for entry in self.audit_log:
            print(entry)

    def voting_process(self):
        """Handles the voting process for multiple voters."""
        print("Welcome to the Enhanced Electronic Voting System\n")
        num_voters = int(input("Enter the number of voters: "))

        for _ in range(num_voters):
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"\nVoting Time: {current_time}")
            
            voter_id = self.generate_voter_id()
            print(f"Your unique voter ID: {voter_id}")

            print("\nCandidates:")
            for idx, candidate in enumerate(self.candidates):
                print(f"{idx + 1}. {candidate}")

            choice = int(input("Enter the number corresponding to your candidate of choice: ")) - 1
            self.cast_vote(voter_id, self.candidates[choice])

        self.tally_votes()
        self.display_results()
        self.display_audit_log()

# Example usage:
candidates = ["Alice", "Bob", "Charlie"]
voting_system = VotingSystem(candidates)
voting_system.voting_process()
