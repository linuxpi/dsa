class Solution {
    public static void main(String[] args) {
        String[] splitArgs = args[0].split("\n");
        Integer i = 0;
        while(i < Integer.parseInt(splitArgs[0])) {
            System.out.println(
                "Case #" + (i + 1) + ": " + new Solution().getNumOps(splitArgs[1 + 2 * i], splitArgs[2 + i * 2]));
            i++;
        }
    }

    public Integer getNumOps(String reacher, String target) {
        Integer totalDiff = 0;

        Integer i = 0;
        while(i<reacher.length()) {
            totalDiff += findClosestChar(reacher.charAt(i), target);
            i++;
        }

        return totalDiff;
    }

    private Integer findClosestChar(char x, String target) {
        // binary search here
        Integer totalChars = target.length();
        Integer start = 0;
        Integer end = totalChars - 1;
        Integer mid = start + (end - start) / 2;
        Integer lastCompDiff = 99;
        while (end - start > 1) {
            // System.out.println("iterate");
            // System.out.println(x);
            // System.out.println(start);
            // System.out.println(end);
            // System.out.println(mid);
            char midElement = target.charAt(mid);
            if (midElement == x) {
                return 0;
            } else if (midElement < x) {
                lastCompDiff = getMinOps(midElement, x);
                start = mid;
                mid = start + (end - start) / 2;
            } else {
                lastCompDiff = getMinOps(midElement, x);
                end = mid;
                mid = start + (end - start) / 2;
            }
        }
        // System.out.println("endgame");
        // System.out.println(getMinOps(target.charAt(start), x));
        // System.out.println(getMinOps(target.charAt(end), x));
        return Math.min(getMinOps(target.charAt(start), x), getMinOps(target.charAt(end), x));
    }

    private Integer getMinOps(char x, char y) {
        return Math.abs(x - y);
    }
}