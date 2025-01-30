from itertools import permutations

def findPermutation(s):
    perm = [''.join(p) for p in permutations(s)]
    uni = set(perm)
    return uni

if __name__ == '__main__':
    s = "abc"
    print(findPermutation(s))