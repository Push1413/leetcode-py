def hIndex(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    return len(citations)

if __name__ == '__main__':
    num = [3,0,6,1,5]
    print(hIndex(num))