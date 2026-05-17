class Solution {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }

        int result = 0;
        int point1 = 1;
        int point2 = 2;

        for (int i = 3; i <= n; i++) {
            int temp = point2;
            point2 = point1 + point2;
            point1 = temp;
            result = point2;
        }

        return result;
    }
}
