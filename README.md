# 🔐 Caesar Cipher Encryptor & Decryptor

## 📌 Overview

This project is a simple Caesar Cipher program written in Python. It allows users to encrypt and decrypt text using the Caesar Cipher algorithm.

The program preserves uppercase and lowercase letters while leaving spaces, numbers, and special characters unchanged.

This project was developed to strengthen my understanding of Python programming, string manipulation, loops, functions, and basic cryptography concepts.

---

## ✨ Features

- 🔒 Encrypts plaintext using the Caesar Cipher algorithm
- 🔓 Decrypts encrypted text back to its original form
- 🔠 Preserves uppercase and lowercase letters
- 🔢 Keeps numbers unchanged
- ✍️ Keeps spaces and special characters unchanged
- 🔄 Automatically handles shift values greater than 26
- 🐍 Written in simple and beginner-friendly Python
- 📚 Demonstrates basic cryptography concepts

---

## 🛠️ Technologies Used

- **Python 3**
- **ASCII Character Conversion**
- **String Manipulation**
- **Functions**
- **Loops**
- **Conditional Statements**

---

## 📂 Project Structure

**text
-Caesar-Cipher-Encryptor/
-│
-├── main.py
-├── README.md
-├── LICENSE
-└── .gitignore**

---

## 🔐 How the Caesar Cipher Works

**The Caesar Cipher is a classical encryption technique in which each alphabetic character is shifted by a fixed number of positions in the alphabet.**

For example, if the shift key is 3:

**-A → D
-B → E
-C → F
-D → G**

When the alphabet reaches the end, it starts again from the beginning:

**-X → A
-Y → B
- Z → C**

For decryption, the same shift key is used in the opposite direction

### EXAMPLE
- Original Text:
Hello World

- Shift Key:
3

- Encrypted Text:
Khoor Zruog

- Decrypted Text:
Hello World

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/a2481240-code/Caesar-Cipher-Encryptor.git
```

2. Navigate to the project directory.

```bash
cd Caesar-Cipher-Encryptor
```

3. Run the program.

```bash
python caesar_cipher.py
```

---

💻 Example

Input
===================================
     Caesar Cipher Encryptor
===================================

Enter the text to encrypt: Hello World
Enter the shift key (1-25): 3

Thank you for using Caesar Cipher Encryptor!

---

## 📚 Learning Objectives
This project helped me practice and understand:

- Python functions
- for loops
- Conditional statements
- String manipulation
- User input
- ASCII character conversion
- ord() and chr() functions
- Encryption and decryption logic
- Modulo operation
- Writing clean and readable Python code
- Basic cryptography concepts

## 🚀 Future Improvements
Some possible improvements for this project are:

- Add input validation for invalid shift values
- Add a menu-driven interface
- Allow users to choose between encryption and decryption
- Support file encryption and decryption
- Save encrypted text to a file
- Create a graphical user interface (GUI)
- Add more cryptographic algorithms

---


## 👨‍💻 Author

 **Malik Hammad**

Cyber Security Student

## 📄 License

This project is licensed under the **MIT License**.

See the LICENSE file for more information.

