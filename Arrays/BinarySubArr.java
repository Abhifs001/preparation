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

    //let us see how to optimize 
    




    
    
}
