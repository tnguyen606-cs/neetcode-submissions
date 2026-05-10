class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        /**
        - map = {}
        - str in strs:
            create a frequency array to store character counts in the str
            map the frequency array to the list of strings that have common array
        - return the list of list of anangrams
        time: O(m * n)
        space: O(m * n)
        */

        Map<String, List<String>> groups = new HashMap<>();

        for (String s : strs) {
            int[] chars = new int[26];
            for (char c : s.toCharArray()) {
                chars[c - 'a']++;
            }
            String key = Arrays.toString(chars);
            groups.putIfAbsent(key, new ArrayList<>());
            groups.get(key).add(s);
        }

        return new ArrayList<>(groups.values());
    }
}
