from converter import to_morse, to_regular


valid = False
while not valid:
    language =  input('Please type an option: "M" to convert to Morse, "L" to decode a Morse text: ').lower()
    if language == 'm':
        to_morse()
        valid = True
    elif language == 'l':
        to_regular()
        valid = True
    else:
        print(f'Sorry, but "{language}" is not a valid option. Please try again')

