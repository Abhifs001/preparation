import java.util.HashMap;
import java.util.Map;

public class BinarySubArr {
        public static void main(String[] args) {
        BinarySubArr b = new BinarySubArr();
        int[] nums = {1, 0, 1, 0, 1};
        int goal = 2;
        System.out.println(b.numSubarraysWithSum(nums, goal)); // Output: 4

        }


     public int numSubarraysWithSum(int[] nums, int goal) {
        // 1 0 1 0 1
        //1 
        //1 1 2 2 3 

        int count = 0;
       

        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (sum == goal) {
                    count++;
                }
            }

        }
        return count;

    }

    //let us see how to optimize using hashmap
    // let us first dry run the hasmap approach 
    public int numSubarraysWithSumOptimized(int[] nums, int goal) {
        int count = 0;
        int sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1); // To handle the case when the subarray starts from index 0

        for (int num : nums) {
            sum += num;
            if (map.containsKey(sum - goal)) {
                count += map.get(sum - goal);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }

        return count;
    }

    // The above code uses a hashmap to store the cumulative sum and its frequency
    //let us dry run the above code
        // 1 0 1 0 1
        // sum = 1, map = {0=1, 1=1}
        // sum = 1, map = {0=1, 1=2}
        // sum = 2, map = {0=1, 1=2, 2=1}
        // sum = 2, map = {0=1, 1=2, 2=2}
        // sum = 3, map = {0=1, 1=2, 2=2, 3=1}
        //now we can see that when we reach the sum of 2, we can find the number of subarrays that sum to 2 by checking the map for the key (sum - goal) which is (2 - 2) = 0. The value for this key is 1, so we add this to our count.
        //let us visualize the hashmap at each step:
        // sum = 1, map = {0=1, 1=1} checking for (1 - 2) = -1, not found
        // sum = 1, map = {0=1, 1=2} checking for (1 - 2) = -1, not found
        // sum = 2, map = {0=1, 1=2, 2=1} checking for (2 - 2) = 0, found 1 
        // sum = 2, map = {0=1, 1=2, 2=2} checking for (2 - 2) = 0, found 1
        // sum = 3, map = {0=1, 1=2, 2=2, 3=1} checking for (3 - 2) = 1, found 2
         

}
