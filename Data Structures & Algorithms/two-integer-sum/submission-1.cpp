class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int sizeofArray = nums.size();
        for(int i=0; i<sizeofArray; i++){
            for(int j=i+1; j<sizeofArray; j++){
                if(nums[i]+nums[j] == target){
                    return vector<int>{i,j};
                }
            }
        }
        return {};
    }
};
