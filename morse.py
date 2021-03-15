import argparse
import sys

word_separator = '/'
morse_code = {
    'A': '.-',
    'B': '_...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

def morse(file_handle):
    """
    Function responsible for transforming given data into morse coded data.
    """
    for line in file_handle:
        coded = ''
        for sign in line:
            sign = sign.capitalize()
            if sign in morse_code:
                coded += morse_code[sign]
            elif sign == ' ' and coded[-1] != word_separator:
                coded += word_separator
        print(coded)


def main(arguments):
    """
    Main funcion of the console ui.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('FILENAME')
    args = parser.parse_args(arguments[1:])

    try:
        with open(args.FILENAME, 'r') as file_handle:
            morse(file_handle)
    except IsADirectoryError:
        print('File is a directory.')
    except FileNotFoundError:
        print('File not found.')

if __name__ == "__main__":
    main(sys.argv)