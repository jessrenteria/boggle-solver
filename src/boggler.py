from trie import Trie

def makeGrid(grid_file):
    grid = []
    with open(grid_file, 'r') as f:
        for line in f:
            line = list(map(lambda x: x.upper(), line.strip().split()))
            grid.append(line)
    return grid

def getAllWords(grid, t):
    words = [set() for _ in range(len(grid) * len(grid[0]))]

    def getAllWordsHelper(used, t, s, r, c):
        used = [list(used[i]) for i in range(len(used))]
        used[r][c] = True
        elem = grid[r][c]
        while t != None and elem != "":
            t = t.getNode(elem[0])
            s += elem[0]
            elem = elem[1:]
        if t == None:
            return
        if t.isWord():
            words[len(s) - 1].add(s)
        for y in range(max(0, r - 1), min(len(grid), r + 2)):
            for x in range(max(0, c - 1), min(len(grid[0]), c + 2)):
                if not used[y][x]:
                    getAllWordsHelper(used, t, s, y, x)

    used = [[False] * len(grid[0]) for _ in range(len(grid))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            getAllWordsHelper(used, t, "", r, c)
    return words

