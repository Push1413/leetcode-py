def isValid(s):
    stack = []
    opening = ["(","{","["]
    closing = [")","}","]"]
    length = len(s)
    for i in range(length):
        if s[i] in opening:
            stack.append(s[i])
        if s[i] in closing:
            if len(stack)==0:
                return False
            find = stack[-1]
            if opening.index(find)!=closing.index(s[i]):
                return False
            else:
                stack.pop()

    return len(stack)==0


if __name__ =='__main__':
    print(isValid("[([]])"))