class Trie:
    def __init__(self):
        self.is_word = False
        self.edges = dict()

    def isWord(self):
        return self.is_word

    def addWord(self, word):
        if len(word) == 0:
            self.is_word = True
            return
        if word[0] not in self.edges:
            self.edges[word[0]] = Trie()
        self.edges[word[0]].addWord(word[1:])

    def search(self, word):
        if len(word) == 0:
            return self.is_word
        return word[0] in self.edges and self.edges[word[0]].search(word[1:])

    def getNode(self, word):
        if len(word) == 0:
            return self
        return self.edges[word[0]].getNode(word[1:]) if word[0] in self.edges else None

