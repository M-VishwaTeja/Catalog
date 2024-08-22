Electronic Voting System :

Voting is a method for a group of individuals to make a collective decision or voice their cumulative opinion to arrive at a consensus. The results of a vote can have far reaching consequences due to which it is imperative to maintain integrity by ensuring that there is no scope for fraud or cheating to occur while the votes are being cast. 

It is highly crucial that voting is carried out in a fair and just manner.

User cannot know any information about the vote Votes cannot be tampered

Aim:

Secure and transparent electronic voting to ensure the integrity of the votes of voters while maintaining the simplicity of the system with a user-friendly console-based user interface.

Core Features:

Voter ID Generation:

Incorporates a unique ID for anonymity of the voters to make sure a single voter does not cast the same vote multiple times.

Encryption Of The Votes:

Store the votes in an encrypted form of encryption provided by Fernet. This maintains the confidentiality of the votes so that they cannot be tampered with.

Audit Log:

Relevant activity (e.g., voter ID production, voting, vote counting) shall be time-stamped in an audit log.
The audit log is saved in a file called audit_log.txt for transparency, possible later validation, and that there has been nothing shady.

Tallying and Results:

In this stage, the system counts the encrypted votes, decrypts them, and issues the results of the election in a clear format.
All actions are also properly logged in an audit log.

Timestamped Voting:

The exact time at which each and every vote is stamped for casting is provided by the system—for example, Voting Time: 2024-08-22 12:34:56. .

Flow of the Voting Process:

Initialize the System:

Candidate initialization into the system.

Voting Process:

Each voter logs in to the system and is assigned a unique voter ID before casting their vote.
Vote is highly enciphered and kept safely.

Calculation:

After receiving all the votes, the system decrypts the votes for calculation.
It displays the results and audit log
Storing the Audit Log

The audit log details are stored in text format, which acts as a permanent record of the voting process for further retrieval.

Advantages:
Security: Voting is kept confidential, and there is no way of tampering with the vote since it is highly encrypted and uses unique voter IDs.

Transparency: The audit log is clear on everything that is done, and thus continually supports the trust in the election.

Simplicity: The system does not have to be rocket science; it lays down easy to use and a simple interface using the console.
