# Morse Code Translator

A command line program that translates text to Morse code and Morse code back to text.

## File

- **step_3.py** - the full program, including the Morse code alphabet, translation functions, and the menu loop.

## What it does

Presents a simple menu:

```
0: Exit
1: Translate a word into Morse Code
2: Translate Morse Code to text.
```

- **Option 1** takes a word (letters, numbers, and spaces) and prints its Morse code equivalent.
- **Option 2** takes a string of Morse code, with each letter's symbols separated by a space, and prints the decoded text.

Any character that isn't part of the standard Morse alphabet (A-Z, 0-9, and space) is shown as `?` in the output.

## Requirements

- Python 3

## Usage

Run it from the command line:

```
python3 step_3.py
```

Example:

- Translating `SOS` returns `... --- ...`
- Translating `... --- ...` back returns `SOS`
