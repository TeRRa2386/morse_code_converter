from codes import morse_code, morse_to_text

def to_morse():
    text_to_convert = input('Hi, please type what you like to be converted using Morse Code: ').upper()
    to_morse_list = []

    for letter in text_to_convert:
        if letter in morse_code:
            to_morse_list.append(morse_code[letter])
        else:
            to_morse_list.append(letter)

    text_converted = ' '.join(to_morse_list)
    print(f'This is the result: {text_converted}')


def to_regular():
    text_to_convert = input('Hi, please type or paste your Morse code to be decoded: ')
    words = text_to_convert.strip().split('   ')
    decoded_words = []

    for word in words:
        letters = word.split()
        decoded_letters = []
        for letter in letters:
            decoded_letter = morse_to_text.get(letter, '?')
            decoded_letters.append(decoded_letter)
        decoded_words.append(''.join(decoded_letters))

    text_converted = ' '.join(decoded_words)
    print(f'This is the result: {text_converted}')

