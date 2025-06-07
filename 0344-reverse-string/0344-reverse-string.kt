class Solution {
    fun reverseString(s: CharArray) {
        var start = 0
        var end = s.size -1

        while (start<end){
            var temp = s[end]
            s[end] = s[start]
            s[start] = temp 
            start++
            end--
        }
    }
}