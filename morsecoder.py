from morsecoder_node import *
from morsecoder_dictionary import *

if __name__ == "__main__":
    #This program was created for testing different solutions to decoding morse code
    #Valid morse code is built out of '.', '-', and '/' with spaces after each complete character
    #EX: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
    #Also this only works with the Latin alphabet (a-z) and only outputs in lowercase.
    node_translator = MorseCoderNode()
    node_translator.build_alpha_tree(Node(' '))
    print("Choose an option:")
    print("Translate words to morse code (1) ")
    print("Decode morse code (2)")
    choice = input()
    if choice == '1':
        words = input("Input words to translate: ")
        print(node_translator.translate_alpha_input(words))
    elif choice == '2':
        code = input("Input morse code to decode: ")
        print(node_translator.translate_morse_input(code))
    else:
        print("Error, invalid choice")

