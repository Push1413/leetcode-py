#118
# https://leetcode.com/problems/pascals-triangle/description/

def generate(numRows):
    output = []
    for i in range(numRows):
        temp = [1]
        if i>0:
            prevRow = output[-1]
            for j in range(1,i):
                temp.append(prevRow[j-1] + prevRow[j])
            temp.append(1)
        output.append(temp)
    return output


if __name__ == '__main__':
    print(generate(5))