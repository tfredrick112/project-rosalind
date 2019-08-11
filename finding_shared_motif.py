"""
Project Rosalind : Finding A Shared Motif
Author : D Tony Fredrick
"""

def common_substr(string, seqs, length):
    """
    Finds a common substring of length 'length' for all the strings in seqs.
    Returns an empty string if a common substring of required length does
    not exist.
    """
    for start in range(len(string) - length + 1):
        part = string[start:start+length]
        for seq in seqs:
            if part not in seq:
                break
        else:
            return part
    return ""

def lcs(seqs):
    """
    Returns the longest common substring of all the strings in seqs.
    """
    string = min(seqs, key = len)
    left = 0
    right = len(string) + 1
    while left + 1< right:
        mid = (left + right)//2
        if common_substr(string, seqs, mid) == "":
            right = mid
        else:
            left = mid
    return common_substr(string, seqs, left)

if __name__ == '__main__':
    with open('rosalind_lcsm.txt') as f:
        s = list(filter(None, f.read().split('>')))
    dna = [s[i][s[i].find('\n'):].replace('\n', '') for i in range(len(s))]
    print(lcs(dna))
