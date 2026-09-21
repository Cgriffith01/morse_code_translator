#
#SEC290.13767.FA2022
#Christine Griffith
#Week 5 Homework Assignment
#

ALPHA_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

MORSE_TO_ALPHA = {morse: letter for letter, morse in ALPHA_TO_MORSE.items()}


def translate_to_morse(word):
    """Translate from alpha and return morse code"""
    letters = []
    for letter in word:
        if letter in ALPHA_TO_MORSE:
            letters.append(ALPHA_TO_MORSE[letter])
        else:
            letters.append('?')
    return ' '.join(letters)


def translate_to_alpha(code):
    """Translate from morse to alpha"""
    letters = []
    for symbol in code.split(' '):
        if symbol in MORSE_TO_ALPHA:
            letters.append(MORSE_TO_ALPHA[symbol])
        else:
            letters.append('?')
    return ''.join(letters)


prompt = "\nMorse Code Translator\n\n0: Exit\n1: Translate a word into Morse Code\n2: Translate Morse Code to text.\n"
prompt += "\nPlease make a selection: "

active = True
while active:
    selection = input(prompt)

    if selection == "0":
        active = False

    elif selection == "1":
        word = input("Please enter a word to be translated to morse code: ")
        word = word.upper()
        encoded = translate_to_morse(word)
        print(encoded)

    elif selection == "2":
        code = input("Please enter a code to be translated to text (separate letters with a space): ")
        decoded = translate_to_alpha(code)
        print(decoded)

    else:
        print("Please enter 0, 1 or 2.")
