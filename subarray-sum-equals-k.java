// 560. Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

class Solution {
    public int subarraySum(int[] nums, int k) {
        int ans = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums[j];
                if (sum == k)
                    ans += 1;
            }
        }
        return ans;
    }
}
