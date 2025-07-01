public class KadaneAlgo {

    public static void main(String[] args) {
        KadaneAlgo kadaneAlgo = new KadaneAlgo();
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("Maximum subarray sum is: " + kadaneAlgo.maxSubArray(nums));
        System.out.println("Maximum subarray sum with indices is: " + kadaneAlgo.maxSubArrayIndex(nums));
    }
   

    public int maxSubArray(int[] nums) {
        if (nums == null || nums.length == 0) {
            throw new IllegalArgumentException("Input array must not be empty");
        }

        if (nums.length == 1)
            return nums[0];
        int ans = nums[0];
        int prevSum = nums[0];
        for (int i = 1; i < nums.length; i++) {

            if (nums[i] + prevSum > nums[i]) {
                prevSum += nums[i];

            } else {
                prevSum = nums[i];
            }

            if (prevSum > ans) {
                ans = prevSum;

            }

        }
        return ans;
    }


    // fllow up question:  
    public int maxSubArrayIndex(int[] nums) {
        if (nums == null || nums.length == 0) {
            throw new IllegalArgumentException("Input array must not be empty");
        }
        int tStart = 0 , start = 0, end = 0;
        int ans = nums[0];
        int prevSum = nums[0];
        for (int i = 1; i < nums.length; i++) {

            if (nums[i] + prevSum > nums[i]) {
                prevSum += nums[i];

            } else {
                prevSum = nums[i];
                tStart = i; // Update start index when starting a new subarray
            }

            if (prevSum > ans) {
                ans = prevSum;
                start = tStart; // Update start index when a new maximum is found
                end = i; // Update end index when a new maximum is found

            }

        }

        System.out.println("Maximum subarray starts at index " + start + " and ends at index " + end);
        return ans;
    }

        //how to handle circular array?
        //let us see an example 
        // int[] nums = {1, -2, 3, -2};
        // we can use the same algorithm to find the maximum subarray sum in a circular array
        //in this array , circular subarray is {3, -2, 1} which is the maximum subarray sum
        // we can find the maximum subarray sum in a circular array by finding the maximum subarray sum in the non-circular array and subtracting the minimum subarray sum from the total sum of the array
        //why this logic works? 
        //because the maximum subarray sum in a circular array is either the maximum subarray sum in the non-circular array or the total sum of the array minus the minimum subarray sum
        //but why ? 
   
    public int maxSubarraySumCircular(int[] nums) {
        int total = 0;
        int maxKadane = nums[0], currentMax = 0;
        int minKadane = nums[0], currentMin = 0;

        for (int num : nums) {
            total += num;

            currentMax = Math.max(num, currentMax + num);
            maxKadane = Math.max(maxKadane, currentMax);

            currentMin = Math.min(num, currentMin + num);
            minKadane = Math.min(minKadane, currentMin);
        }

        // If all numbers are negative, return the max single element
        if (maxKadane < 0) return maxKadane;

        return Math.max(maxKadane, total - minKadane);
    }
 

}       
