import argparse
import time

from trie import Trie
import anagrammer
import boggler

def makeTrie(dict_file):
    tree = Trie()
    with open(dict_file, 'r') as f:
        for word in f:
            tree.addWord(word.strip().upper())
    return tree

def writeWords(found_file, words):
    with open (found_file, 'w') as f:
        for length in range(len(words) - 1, 0, -1):
            for word in words[length]:
                f.write(word + '\n')

def main():
    parser = argparse.ArgumentParser(description="Word Finder")
    parser.add_argument('dict', type=str, help="a file containing a list of valid words")
    parser.add_argument('found', type=str, help="a file to dump found words")
    args = parser.parse_args()
    print("Making trie...")
    start = time.time()
    trie = makeTrie(args.dict)
    elapsed = time.time() - start
    print("Made trie in {:.4f} seconds.".format(elapsed))

    while True:
        print("> ", end='')
        command = input()
        if command == 'q' or command == "quit" or command == "exit":
            print("Bye!")
            break
        command = command.split()
        if (len(command) != 2
            or (command[0] != "anagrammer" and command[0] != "boggler")):
            print("Usage: (anagrammer seq_file|boggler grid_file)")
            continue

        words = []
        print("Finding words...")
        start = time.time()
        if command[0] == "anagrammer":
            seq = anagrammer.makeSeq(command[1])
            words = anagrammer.getAllWords(seq, trie)
        elif command[0] == "boggler":
            grid = boggler.makeGrid(command[1])
            words = boggler.getAllWords(grid, trie)

        elapsed = time.time() - start
        print("Found all words in {:.4f} seconds.".format(elapsed))
        writeWords(args.found, words)

if __name__ == "__main__":
    main()
