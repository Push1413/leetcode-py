class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()

        def isValid(expr):
            count =0
            for char in expr:
                if char =='(':
                    count+=1
                if char ==')':
                    count -=1
                if count <0:
                    return False
            return count ==0
        
        def cal(expr):
            left = right=0
            for char in expr:
                if char =='(':
                    left +=1
                elif char ==')':
                    if left>0:
                        left-=1
                    else:
                        right+=1
            
            return left,right
        
        def dfs(index,path,left_rem,right_rem):
            if index == len(s):
                if left_rem==0 and right_rem==0 and isValid(path):
                    res.add(path)
                return
            
            char = s[index]

            if char=='(':
                if left_rem>0:
                    dfs(index+1,path,left_rem-1,right_rem)
                dfs(index+1,path+char,left_rem,right_rem)
            
            elif char ==')':
                if right_rem>0:
                    dfs(index+1,path,left_rem,right_rem-1)
                dfs(index+1,path+char,left_rem,right_rem)
            
            else:
                dfs(index+1,path+char,left_rem,right_rem)
        

        left_rem,right_rem = cal(s)
        dfs(0,"",left_rem,right_rem)

        return list(res)
                    






        