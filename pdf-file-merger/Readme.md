# PDF Merger

A simple Python application that merges multiple PDF files into a single PDF. The program automatically scans the input folder, merges all PDF files in alphabetical order, ignores non-PDF files, and saves the merged document to an output folder.

---

## Features

- Merge multiple PDF files into one
- Automatically detects PDF files
- Creates the output folder automatically
- Saves the merged PDF with a custom name
- Clean and beginner-friendly code
- Exception handling for invalid paths or missing files

---

## Technologies Used

- Python 
- pypdf
- os

---

## Project Structure

```
PDF-Merger/
│
├── input_pdf/
│   ├── example_1.pdf
│   ├── example_2.pdf
│   ├── example_3.pdf
│   ├── example_4.pdf
│   ├── example_5.pdf
│   ├── example_6.pdf
│
├── output_pdf/
│   └── merged_pdf.pdf
│
├── main.py
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/abdulsbaheen/PDF-Merger.git
```

Move into the project folder

```bash
cd PDF-Merger
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Requirements

```
pypdf
```

or install manually

```bash
pip install pypdf
```

---

## Usage

Run the program

```bash
python main.py
```

The program will:

- Scan the `input_pdf` folder
- Ignore non-PDF files
- Merge all PDF files
- Create the `output_pdf` folder if needed
- Save the final file as:

```
output_pdf/merged_pdf.pdf
```

---

## Example

### Input Folder

```
input_pdf/
│
├── example_1.pdf
├── example_2.pdf
├── example_3.pdf
├── example_4.pdf
├── example_5.pdf
├── example_6.pdf
```

### Output Folder

```
output_pdf/
│
└── merged_pdf.pdf
```

---

## Learning Outcomes

This project demonstrates:

- File handling
- Working with directories
- Filtering files by extension
- Exception handling
- Functions
- PDF manipulation using `pypdf`
- Python project organization

---

## Future Improvements

- Drag-and-drop PDF support
- GUI using Tkinter
- Merge PDFs in custom order
- Password-protected PDF support
- Progress bar
- Command-line arguments
- Merge PDFs from multiple folders

---

## Author

**Abdul Rehman**

GitHub: https://github.com/abdulsbaheen

---

## License

This project is licensed under the MIT License.
