CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  ' ': '|'
        }

reverse_code = {value: key for key, value in CODE.items()}


def to_morse(user_input):
    return ''.join(CODE.get(x.upper()) for x in user_input)


def to_english(user_input):
    return ''.join(reverse_code.get(x) for x in user_input.split())


choice = input("Type M to convert into morse, or type E to convert to English: ")
user_input = input("What would you like to translate? ")
if choice == 'M':
    print(to_morse(user_input))
else:
    print(to_english(user_input))
















# def convert_to(user_input):
#     morse_code = {'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ',
#                   'G': '--. ', 'H': '.... ', 'I': '.. ', 'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
#                   'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ', 'Q': '--.- ', 'R': '.-. ',
#                   'S': '... ', 'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ',
#                   'Y': '-.-- ', 'Z': '--.. ', '0': '----- ', '1': '.---- ', '2': '..--- ',
#                   '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ',
#                   '9': '----. ', ' ': '|'}
#     code = ""
#
#     for char in user_input:
#         code += morse_code[char.upper()]
#
#     return code
#
#
# user_input = input("Enter a word or phrase to convert into Morse Code: ")
# print(convert_to(user_input))











