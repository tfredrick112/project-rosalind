from itertools import permutations

with open('rosalind_lexf.txt') as f:
    s = [line[:-1] for line in f.readlines()]
n = int(s[1])
letters = s[0].replace(' ', '')

words = list(permutations(letters * n, n))
words = list(set([''.join(word) for word in words]))
words = sorted(words)
for w in words:
    print(w)
