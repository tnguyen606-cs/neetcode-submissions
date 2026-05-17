class Solution {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        Map<Integer, Integer> memo = new HashMap<>();
        memo.put(1, 1);
        memo.put(2, 2);

        for (int i = 3; i <= n; i++) {
            int count = memo.get(i - 1) + memo.get(i -2);
            memo.put(i, count);
        }

        return memo.get(n);
        
    }
}
