# String trie
Trie = {}

def add(word):
    temp = Trie
    for ch in word:
        if ch not in temp:
            temp[ch] = [0, {}]
        temp[ch][0] += 1
        temp = temp[ch][1]

def count_prefix(prefix):
    temp = Trie
    n = 0
    for c in prefix:
        if c not in temp:
            return 0
        n = temp[c][0]
        temp = temp[c][1]
    return n
