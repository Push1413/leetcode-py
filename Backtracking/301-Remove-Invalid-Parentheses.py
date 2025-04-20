def removeInvalidParentheses(s):
    res = set()

    def get_misplaced(s):
        left = right = 0
        for char in s:
            if char =='(':
                left +=1
            elif char ==')':
                if left>0:
                    left -=1
                else:
                    right +=1
        return left, right

    def isValid(expr):
        count = 0
        for char in expr:
            if char =='(':
                count+=1
            elif char ==')':
                count -=1
            if count<0:
                return False
        return count==0

    def dfs(index, left_rem, right_rem, path):
        if index==len(s):
            if left_rem==0 and right_rem==0 and isValid(path):
                res.add(path)
            return

        c = s[index]

        if c =='(':
            # Option 1: Remove this '('
            if left_rem>0:
                dfs(index+1, left_rem-1, right_rem, path)
            # Option 2: Keep it
            dfs(index+1, left_rem, right_rem, path+c)

        elif c ==')':
            # Option 1: Remove this ')'
            if right_rem>0:
                dfs(index+1, left_rem, right_rem-1, path)
            # Option 2: Keep it
            dfs(index+1, left_rem, right_rem, path+c)

        else:
            # Keep letters as is
            dfs(index+1, left_rem, right_rem, path+c)

    # Kick off
    left_rem, right_rem = get_misplaced(s)
    dfs(0, left_rem, right_rem,"")

    return list(res)


if __name__=='__main__':
    print(removeInvalidParentheses("()())()"))