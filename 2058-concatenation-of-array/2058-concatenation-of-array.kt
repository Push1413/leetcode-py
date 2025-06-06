class Solution {
    fun getConcatenation(nums: IntArray): IntArray {
        val len = nums.size
        val ans = IntArray(2*len)

        for(i in 0 until len){
            ans[i] = nums[i]
            ans[len+i] = nums[i]
        }
        return ans
    }
}