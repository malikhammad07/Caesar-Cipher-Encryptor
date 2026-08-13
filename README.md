# Caesar-Cipher-Encryptor

A simple Python program that encrypts and decrypts text using the Caesar Cipher technique.

## Features

- Encrypt text using a shift key
- Decrypt encrypted text
- Supports uppercase and lowercase letters
- Keeps spaces, numbers, and symbols unchanged
- Uses a shift key from 1 to 25

## Requirements

- Python 3.x

## How to Run

Open the terminal in the project folder and run:

```bash
python main.py

How It Works

The Caesar Cipher shifts each letter by a fixed number of positions in the alphabet.
A → D
B → E
C → F
For decryption, the same shift key is used in the opposite direction.
Example
===================================
     Caesar Cipher Encryptor
===================================

Enter the text to encrypt: Hello World
Enter the shift key (1-25): 3

===================================
Original Text : Hello World
Shift Key     : 3
===================================
Encrypted Text : Khoor Zruog
Decrypted Text : Hello World
===================================
Thank you for using Caesar Cipher Encryptor!
For example, with a shift key of 3:

Project Structure
Caesar-Cipher-Encryptor/
├── main.py
├── README.md
├── LICENSE
└── .gitignore
License

This project is licensed under the MIT License.
### README save karne ke baad

Terminal mein:

```powershell
git add README.md
git commit -m "Update README"
git push
