import java.util.HashMap;

class Subarr {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 };

        longestSubarray(arr, 0);
    }

    /**
     * This method finds the length of the longest subarray whose sum equals k.
     * 
     * @param nums The input array of integers.
     * @param k    The target sum for the subarray.
     * @return The length of the longest subarray with sum equal to k.
     */

    public static int longestSubarray(int[] nums, int k) {
        int len = 0;

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                int sum = 0;
                int tempAns = 0;
                for (int start = i; start <= j; start++) {
                    sum += nums[start];
                    tempAns++;
                }
                if (sum == k) {
                    len = Math.max(len, tempAns);
                }

            }
        }
        return len;
    }

    /**
     * This method finds the length of the longest subarray whose sum equals k using
     * a more efficient approach.
     * 
     * @param nums The input array of integers.
     * @param k    The target sum for the subarray.
     * @return The length of the longest subarray with sum equal to k.
     */
    public static int longestSubarray2(int[] nums, int k) {
        int len = 0;
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (sum == k) {
                    len = Math.max(len, j - i + 1);
                }
            }
        }
        return len;
    }

    public int longestSubarray3(int[] nums, int k) {

        int left = 0, right = 0, len = 0;
        int sum = 0;
        for (right = 0; right < nums.length; right++) {
            sum += nums[right];

            while (sum > k && left <= right) {
                sum -= nums[left];
                left++;
            }
            if (sum == k) {
                len = Math.max(len, right - left + 1);
            }
        }
        return len;
    }

    public int longestSubarray4(int[] nums, int k) {

        int left = 0, right = 0, len = 0;
        int sum = 0;     
        HashMap<Integer, Integer> map = new HashMap<>();

        for (right = 0; right < nums.length; right++) {
            sum += nums[right];

            if (sum == k) {
                len = Math.max(len, right+1);
            }
            map.putIfAbsent(sum, right);
            if (map.containsKey(sum - k)) {
                len = Math.max(len, right - map.get(sum - k));
            }
            // while (sum > k && left <= right) {
            //     sum -= nums[left];
            //     left++;
            // }
             
        }
        return len;
    }

}