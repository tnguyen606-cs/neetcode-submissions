class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> numMap = new HashMap<>();

        /**
        Time: O(n)
        Space: O(n)
        */
        for (int num: nums) {
            if (numMap.containsKey(num)) {
                return true;
            }
            numMap.put(num, 1);
        }

        return false;
    }
}