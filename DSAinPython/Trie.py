class Trie:
    def __init__(self, character, is_terminal):
        self.character = character
        self.children = {}
        self.is_terminal = is_terminal

    def is_prefix(self, word, index):
        if index == len(word):
            return False

        next_char = word[index]
        if next_char not in self.children:
            return False

        return self.children[next_char].is_prefix(word, index+1)