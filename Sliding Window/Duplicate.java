import java.util.HashSet;

class Duplicate {
    //1 2 3 1 
    //1 2 3 1 
    //0 1 2 3 4 5  
//  /[1,2,3,1,2,3]
    // abs i - j <=k and check elei=elej
    
    public static void main(String[] args) {
        Duplicate d = new Duplicate();
        int[] nums = {1, 2, 3, 1};
        int k = 3;
        System.out.println(d.containsNearbyDuplicate(nums, k)); // true
        nums = new int[]{1, 2, 3, 4};
        k = 2;
        System.out.println(d.containsNearbyDuplicate(nums, k)); // false
    }
    //problem: https://leetcode.com/problems/contains-duplicate-ii/
    //problem is that it checks pairs only once not all possible pairs withing k distance

    public boolean containsNearbyDuplicate(int[] nums, int k) {
        if (k==0)return false;
        int left = 0 ; 
        int right = 1 ; 

        while (right<nums.length){
            //shrink window if it is > k 
            if(Math.abs(left-right)>k){
                left++; 
            }

            if(Math.abs(left-right)<=k && nums[left]==nums[right]){
                return true;
            }
            right++;
        }

        return false;
    }
    
      public boolean containsNearbyDuplicate2(int[] nums, int k) {
        HashSet<Integer>st = new HashSet<>() ; 

        for(int i=0;i<nums.length;i++){
            if(st.contains(nums[i])){
                return true;
            }

            st.add(nums[i]); 


            if(st.size()>k){
                st.remove(nums[i-k]);
            }
        }

        return false;
    }

}