# QR Code Generator

A Python-based QR Code Generator that creates high-quality QR codes for different types of data such as websites, text, phone numbers, email addresses, and Wi-Fi passwords. The project also supports adding a custom logo to the center of the QR code and automatically saves the generated image inside a user-defined folder.

---

## Features

- Generate QR codes instantly
- Supports multiple data types
  - Website URLs
  - Phone Numbers
  - Email Addresses
  - Plain Text
  - Wi-Fi Passwords
- Optional logo embedding
- Automatic folder creation
- Save QR codes with custom filenames
- Simple command-line interface
- High error correction for logo support

---

## Technologies Used

- Python 
- qrcode
- Pillow (PIL)
- os (built-in)

---

## Project Structure

```
QR-Code-Generator/
│
├── lesson.py               # Basic QR code generator
├── lesson_01.py            # Save QR code with custom filename
├── lesson_02.py            # Menu-driven QR generator
├── lesson_03.py            # Advanced version with logo support
│
├── logo.png                # Sample logo
├── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/abdulsbaheen/QR-Code-Generator.git
```

Move into the project directory

```bash
cd QR-Code-Generator
```

Install the required libraries

```bash
pip install qrcode pillow
```

---

## Usage

Run the advanced version

```bash
python lesson_03.py
```

Follow the prompts:

1. Enter the data to encode.
2. Choose whether to add a logo.
3. Provide the logo path (optional).
4. Enter the folder name.
5. Enter the output filename.

The generated QR code will be saved automatically.

---

## Example

```
Enter the data:
https://github.com

Add logo?
1 = Yes
0 = No

Folder Name:
Output

File Name:
github_qr.png
```

Output

```
Output/
└── github_qr.png
```

---

## Requirements

- Python 3.8+
- qrcode
- Pillow

Install dependencies

```bash
pip install qrcode pillow
```

---

## Future Improvements

- GUI using Tkinter
- Generate colored QR codes
- Support different image formats
- Batch QR code generation
- Drag-and-drop logo selection
- Custom QR code sizes
- Error handling and input validation

---

## Learning Outcomes

This project helped me practice:

- Functions
- Conditional statements
- File handling
- Folder creation using `os`
- Working with external libraries
- Image processing using Pillow
- QR code generation
- Python project organization

---

## Author

**Abdul Rehman**

GitHub: https://github.com/your-username

---

## License

This project is licensed under the MIT License.
