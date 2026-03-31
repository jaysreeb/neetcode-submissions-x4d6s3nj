class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        // Condtion to check duplicates if(number[i]=== number[i+1])
        for(let i=0; i< nums.length-1; i++){
            if(nums[i] === nums[i+1]){
                nums.splice(i, 1);
                i--;
            }
        }
        return nums.length;
    }
}
