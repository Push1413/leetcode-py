s="aaa"
sublist = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        temp = s[i:j]
        if temp == temp[::-1]:
            sublist.append(temp)
print(len(sublist), sublist)
