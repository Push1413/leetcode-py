class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ["", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
        teens = ["", " Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
        thousand = ["", " Thousand", " Million", " Billion"]

        def helper(x):
            if x<20:
                return ones[x]
            elif x<100:
                return teens[x//10] + helper(x%10)
            elif x<1000:
                return helper(x//100) + " Hundred" + helper(x%100)
            else:
                for i in range(3,0,-1):
                    if x>= 1000 ** i:
                        return helper(x// (1000 ** i)) + thousand[i] + helper(x % (1000 ** i))
            
            return ''
            

        if num ==0:
            return 'Zero'
        return helper(num).lstrip()

            
            

                


        