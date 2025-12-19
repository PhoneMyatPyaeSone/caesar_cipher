# Caesar Cipher Encryption Tool 🔐

A simple **Python command-line application** that performs **Caesar Cipher encryption and decryption**.  
This program allows users to shift letters in a message by a given key to encrypt or decrypt text interactively.

---

## 📌 Features

- Encrypt plain text using Caesar Cipher  
- Decrypt cipher text using the same shift key  
- Supports **uppercase and lowercase letters**  
- Preserves spaces in text  
- Colorized ASCII banner using `colorama`  
- Interactive menu-based interface  

---

## 🧠 What is Caesar Cipher?

The **Caesar Cipher** is a classic substitution cipher where each letter in the text is shifted forward or backward by a fixed number of positions in the alphabet.

**Example (Shift = 3):**

```
Plain Text : HELLO
Cipher     : KHOOR
```

---

## 🛠 Requirements

- Python **3.x**
- `colorama` library

Install `colorama` if it is not already installed:

```bash
pip install colorama
```

---

## 🚀 How to Run

1. Clone or download this repository  
2. Navigate to the project directory  
3. Run the program:

```bash
python app.py
```

---

## 📖 Usage

When the program starts, you will see a menu:

```
Choose Method
1. Encrypt
2. Decrypt
3. Exit
```

### 🔒 Encrypt
- Enter the plain text
- Enter a shift number (for example: `3`)

### 🔓 Decrypt
- Enter the cipher text
- Enter the same shift number used during encryption

---

## 🧪 Example

### Encryption

```
Plain Text : Hello World
Shift Key  : 3
Cipher     : Khoor Zruog
```

### Decryption

```
Cipher Text : Khoor Zruog
Shift Key   : 3
Plain Text  : Hello World
```

---

## 📂 Project Structure

```
.
├── app.py
└── README.md
```

---

## 👨‍💻 Author

**PhoneMyatPyaeSone**  
GitHub: [@PhoneMyatPyaeSone](https://github.com/PhoneMyatPyaeSone)

---

## 📜 License

This project is open-source and free to use for **learning and educational purposes**.
