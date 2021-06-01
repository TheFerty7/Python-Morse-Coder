#Node tree solution, pretty slow but was fun to create.
#If you have an idea of how to make this better in any way, please make a branch for it and let me know! 
#I want to see how other people would do this.
import string

class Node:
    def __init__(self, data):
        self.parent = None
        self.type = None
        self.dot = None
        self.dash = None
        self.data = data

    def insert_dot(self, node):
        if self.dot is None:
            self.dot = node
    
    def insert_dash(self, node):
        if self.dash is None:
            self.dash = node

    #sets the childrens parent as the calling node
    def set_children(self, dot_node, dash_node):
        if dot_node:
            dot_node.parent = self
            dot_node.type = '.'
        if dash_node:
            dash_node.parent = self
            dash_node.type= '-'
        self.dot = dot_node
        self.dash = dash_node

class MorseCoderNode:
    node_dictionary = {}
    top_node = None
    valid_inputs = ['.', '-', ' ', '/']

    def __init(self):
        pass

    def build_alpha_tree(self, top_node):
        self.top_node = top_node
        alphabet = list(string.ascii_lowercase)
        nodes = []
        for item in alphabet:
            nodes.append(Node(item))
        
        self.node_dictionary = dict(zip(alphabet, nodes))
        self.top_node.set_children(self.node_dictionary['e'], self.node_dictionary['t'])
        self.node_dictionary['e'].set_children(self.node_dictionary['i'], self.node_dictionary['a'])
        self.node_dictionary['i'].set_children(self.node_dictionary['s'], self.node_dictionary['u'])
        self.node_dictionary['s'].set_children(self.node_dictionary['h'], self.node_dictionary['v'])
        self.node_dictionary['u'].set_children(self.node_dictionary['f'], None)
        self.node_dictionary['a'].set_children(self.node_dictionary['r'], self.node_dictionary['w'])
        self.node_dictionary['w'].set_children(self.node_dictionary['p'], self.node_dictionary['j'])
        self.node_dictionary['r'].set_children(self.node_dictionary['l'], None)
        self.node_dictionary['t'].set_children(self.node_dictionary['n'], self.node_dictionary['m'])
        self.node_dictionary['m'].set_children(self.node_dictionary['g'], self.node_dictionary['o'])
        self.node_dictionary['g'].set_children(self.node_dictionary['z'], self.node_dictionary['q'])
        self.node_dictionary['n'].set_children(self.node_dictionary['d'], self.node_dictionary['k'])
        self.node_dictionary['d'].set_children(self.node_dictionary['b'], self.node_dictionary['x'])
        self.node_dictionary['k'].set_children(self.node_dictionary['c'], self.node_dictionary['y'])

    #translate the morse code by stepping down through a node tree
    def translate_morse_input(self, morse_code):
        current_node = self.top_node
        current_word = []
        final_sentence = []
        for char in morse_code:
            if char not in self.valid_inputs:
                print(f'Error: Invalid input. Found: {char}')
                return
            else:
                if char == '.':
                    current_node = current_node.dot
                elif char == '-':
                    current_node = current_node.dash
                elif char == ' ':
                    current_word.append(current_node.data)
                    current_node = self.top_node
                elif char == '/':
                    final_sentence.append(''.join(current_word))
                    current_node = self.top_node
                    current_word = []

        #catch final character if the end of the code was a '/'
        if current_node is not self.top_node:
            current_word.append(current_node.data)

        final_sentence.append(''.join(current_word))
        return ''.join(final_sentence)

    #Reads the tree upwards from the designated node and returns the code
    def search_tree_up(self, node, word):
        if node.parent is not None:
            word.append(node.type)
            self.search_tree_up(node.parent, word)
        return word[::-1]

    def translate_alpha_input(self, sentence):
        translated_sentence = []
        for char in sentence:
            try:
                current_node = self.node_dictionary[char.lower()]
                current_char = [' ']
                final_char = ''.join(self.search_tree_up(current_node, current_char))
                translated_sentence.append(final_char)
            except:
                if char.isspace():
                    translated_sentence.append('/ ')

        return ''.join(translated_sentence)

