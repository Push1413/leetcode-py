class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> prefixSumCount = new HashMap<>();
        prefixSumCount.put(0, 1);
        int currentSum = 0;
        int result = 0;
        for (int num:nums){
            currentSum +=num;
            if (prefixSumCount.containsKey(currentSum-k)){
                result += prefixSumCount.get(currentSum-k);
            }
            prefixSumCount.put(currentSum, prefixSumCount.getOrDefault(currentSum, 0) + 1);
        }
        return result;
        
    }
}