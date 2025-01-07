def isAnagram(s: str, t: str) -> bool:
    hashTable = {}
    for char in s:
        hashTable[char] = hashTable.get(char,0)+1
    for char in t:
        hashTable[char] = hashTable.get(char,0)-1
    for key, values in hashTable.items():
        if hashTable.get(key)!=0:
            return False

    return True

s="anagram"
t="nagaram"
print(isAnagram(s,t))



