# Text Encryption Tool

A Python-based command-line tool for encrypting and decrypting sentences using a custom algorithm.

**Repository:** [github.com/himanshu0154/text-encryption-tool](https://github.com/himanshu0154/text-encryption-tool)  
**Main File:** `main.py`

---

## Features

- Encrypts words using a rotation and random string wrapping mechanism.
- Decrypts previously encrypted sentences.
- Stores encrypted messages temporarily during session.
- Option to clear stored messages or exit the tool.

---

## Encryption Logic

- Words **less than 3 characters** are reversed.
- Words **3+ characters** are:
  - Rotated (first letter moved to the end).
  - Wrapped with 3 random lowercase letters (prefix and suffix).

**Example:**
- Input: `hello`
- Encrypted: `abcellohxyz` (where `abc` and `xyz` are random strings)

---

## Decryption Logic

- For short words (<3): reversed again.
- For others:
  - Remove the prefix and suffix.
  - Move the last letter to the front.

---

## Usage

### Prerequisites

- Python 3.x

### Run the script

    ```bash
    python main.py
    
# Command

e → Encrypt a sentence

d → Decrypt a previously encrypted sentence

clear → Clear the list of encrypted sentences

stop → Exit the program

# Example 

    ```bash
    what would you wanna do (encrypted(e)/decrypted(d)/stop/clear): e
    enter the word: hello world
    Encrypted: abchelloxyz defworlduvw

    what would you wanna do (encrypted(e)/decrypted(d)/stop/clear): d
    please choose from these words :
    1. abchelloxyz defworlduvw
    enter your the number respect to the sentence you want to choose: 1
    Decrypted: hello world
    

# Repository Structure

    ```bash
    text-encryption-tool/
    ├── main.py  # Main encryption script
    

# License

This project is licensed under the MIT License.

# Author

by [himanshu0154](https://github.com/himanshu0154)