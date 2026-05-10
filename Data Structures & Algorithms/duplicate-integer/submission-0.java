class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> uniqueNums = new ArrayList<>();

        /**
        Time: O(n)
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