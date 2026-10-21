class Solution {
    public int minOperations(String s) {
        int n = s.length();
        boolean sorted = true;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) < s.charAt(i - 1)) {
                sorted = false;
                break;
            }
        }
        if (sorted) {
            return 0;
        }
        if (n == 2) {
            return -1;
        }
        char min = 'z';
        char max = 'a';
        int minCount = 0, maxCount = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c < min) {
                min = c;
                minCount = 1;
            } else if (c == min) {
                minCount++;
            }
            if (c > max) {
                max = c;
                maxCount = 1;
            } else if (c == max) {
                maxCount++;
            }
        }
        char first = s.charAt(0);
        char last = s.charAt(n - 1);
        if (first == min || last == max) {
            return 1;
        }
        if (first == max && maxCount == 1 &&
            last == min && minCount == 1) {
            return 3;
        }
        return 2;
    }
}