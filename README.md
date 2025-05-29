
# Morse Code Converter — Python Console App

This is a simple command-line tool that allows users to convert between plain text and Morse code. It supports letters (A–Z), numbers (0–9), and spaces. The program includes input validation and prints the result directly to the console.

---

## Features

- Convert plain text to Morse code
- Decode Morse code back to text
- Handles spaces and unknown characters
- Simple and user-friendly console interface
- Organized using separate modules for logic and data

---

## Project Structure

```
morse_converter/
│
├── main.py            # Entry point — handles user input and menu
├── converter.py       # Conversion logic: to_morse() and to_regular()
├── codes.py           # Morse code dictionaries
└── README.md          # Project documentation
```

---

## Requirements

- Python 3.7 or higher
- No external libraries required

---

## How to Run

1. Clone this repository or download the files.
2. In a terminal, navigate to the project directory.
3. Run the main script:

```
python main.py
```

4. Follow the on-screen instructions:
   - Type "M" to convert text to Morse code.
   - Type "L" to decode Morse code back to plain text.

---

## Notes

- Words in Morse code are separated by three spaces.
- Characters are separated by one space.
- Unknown or unsupported characters are replaced with `?` during decoding.

---

## License

This project is for educational and personal use.
