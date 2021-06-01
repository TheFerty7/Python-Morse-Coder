import string

class MorseCoderDictionary:
    morsecode_dictionary = {}

    def __init__(self):
        self.generate_dictonary()

    def generate_dictonary(self):
        #Unfortunately there's no pattern to morse code (unless I'm blind) so I just built the dictionary manually.
        #Each letter's code was designed to be inversely related to the frequency of its occurence.
        #"E" is the most common letter in English so it has the shortest code "."
        self.morsecode_dictionary = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": "-.--",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }
