class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int n = nums.size();
        int r=-1;
        int mi =nums[0];
        for (int i=0;i<n;i++){
            if (nums[i]> mi){
                r=max(r,nums[i]-mi);
            }
            mi=min(mi,nums[i]);
        }
        return r;
    }
};