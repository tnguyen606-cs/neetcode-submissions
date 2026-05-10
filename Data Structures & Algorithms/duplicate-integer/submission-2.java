class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> uniqueNums = new ArrayList<>(nums.length);

        /**
        Time: O(n^2)
        Space: O(n)
        */
        for (int num: nums) {
            if (uniqueNums.contains(num)) {
                return true;
            }
            uniqueNums.add(num);
        }

        return false;
    }
}