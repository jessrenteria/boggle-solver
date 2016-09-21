from trie import Trie

def makeSeq(seq_file):
    seq = []
    with open(seq_file, 'r') as f:
        seq = list(map(lambda x: x.upper(), f.read().strip().split()))
    return seq

def getAllWords(seq, t):
    words = [set() for _ in range(len(seq))]

    def getAllWordsHelper(used, t, s, idx):
        used = list(used)
        used[idx] = True
        elem = seq[idx]
        while t != None and elem != "":
            t = t.getNode(elem[0])
            s += elem[0]
            elem = elem[1:]
        if t == None:
            return
        if t.isWord():
            words[len(s) - 1].add(s)
        for x in range(len(seq)):
            if not used[x]:
                getAllWordsHelper(used, t, s, x)

    used = [False for _ in range(len(seq))]
    for idx in range(len(seq)):
        getAllWordsHelper(used, t, "", idx)
    return words

