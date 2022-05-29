def convert_to(user_input):
    morse_code = {'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ',
                  'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
                  'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ', 'Q': '--.- ', 'R': '.-. ',
                  'S': '... ', 'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
                  'Y': '-.-- ', 'Z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ',
                  '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ',
                  '9': '----. ', ' ': '|'}
    code = ""

    for char in user_input:
        code += morse_code[char.upper()]

    return code


user_input = input("Enter a word or phrase to convert into Morse Code: ")
print(convert_to(user_input))