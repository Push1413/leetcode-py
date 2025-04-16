class Solution {
    public int[] productExceptSelf(int[] nums) {
        int size  = nums.length;
        int[] prefixProd = new int[size];
        int[] postfixProd = new int[size];
        int[] result = new int[size];
         prefixProd[0]=1;
         postfixProd[size-1]=1;

        for(int i=1;i<size;i++){
            prefixProd[i] = nums[i-1] * prefixProd[i-1];
        }

        for(int j=size-2;j>=0;j--){
            postfixProd[j]= nums[j+1] * postfixProd[j+1];
        }

        for (int k=0;k<size;k++){
            result[k] = prefixProd[k] * postfixProd[k];
        }

        return result;
    }
}