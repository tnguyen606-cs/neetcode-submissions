class Solution {
    public boolean hasDuplicate(int[] nums) {
        /**
        Time: O(n^2)
        Space: O(1)
        */

        for (int index = 0; index < nums.length; index++) {
            for (int j = index + 1; j < nums.length; j++) {
                if (nums[index] == nums[j]) {
                    return true;
                }
            }
        }

        return false;
    }
}