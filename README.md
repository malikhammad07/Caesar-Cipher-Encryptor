# Caesar-Cipher-Encryptor
Overview
This project is a simple Caesar Cipher program written in Python. It allows users to encrypt and decrypt text using the Caesar Cipher algorithm. The program preserves uppercase and lowercase letters while leaving spaces, numbers, and special characters unchanged.

This project was developed to strengthen my understanding of Python programming, string manipulation, loops, functions, and basic cryptography concepts.

Features
Encrypts plaintext using the Caesar Cipher algorithm
Decrypts encrypted text back to its original form
Preserves uppercase and lowercase letters
Keeps spaces, numbers, and special characters unchanged
Automatically handles shift values greater than 26
Clean and beginner-friendly Python code
Technologies Used
Python 2
Project Structure
Caesar-Cipher-Encryptor/
│
├── caesar_cipher.py
├── README.md
├── LICENSE
└── .gitignore
How the Algorithm Works
The Caesar Cipher is one of the oldest encryption techniques. Each alphabetic character in the input text is shifted by a fixed number of positions in the alphabet.

For example:

Shift Key: 3
A → D
B → E
X → A
Y → B
Z → C
The same shift key is used in reverse to decrypt the encrypted text.

How to Run
Clone the repository.
git clone https://github.com/malikhammad07/Caesar-Cipher-Encryptor.git
Navigate to the project directory.
cd Caesar-Cipher-Encryptor
Run the program.
python caesar_cipher.py
Example
Input
Enter the text to encrypt: Hello World
Enter the shift key (1-25): 3
Output
Original Text : Hello World
Shift Key     : 3

Encrypted Text : Khoor Zruog
Decrypted Text : Hello World
Learning Objectives
This project helped me practice:

Python functions
For loops
Conditional statements
String manipulation
ASCII character conversion using ord() and chr()
Encryption and decryption logic
Writing clean and readable code
Future Improvements
Add input validation for invalid shift values
Support file encryption and decryption
Add a menu-driven interface
Create a graphical user interface (GUI)
Save encrypted text to a file
Author
Malik Hammad

Cyber Security Student

License
This project is licensed under the MIT License
