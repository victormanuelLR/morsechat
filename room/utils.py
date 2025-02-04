from unidecode import unidecode

def translate_to_morse_code (message: str):

    translated_message = ''
    message = unidecode(message.upper())
    print(message)
    morse_dict = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',  
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',  
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',  
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
        'Z': '--..',  '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '+': '.-.-.', '-': '-....-','*': '-..-',  '/': '-..-.', 
        '=': '-...-', '?': '..--..','!': '-.-.--','.': '.-.-.-',',': '--..--',
        ':': '---...',' ': '/'   
    }
    for symbol in message:
        if symbol in morse_dict:
            translated_message += morse_dict[symbol] + ' '
        else : 
            translated_message += '?'


    return translated_message


