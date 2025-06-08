class RotateArr {
    public static void main(String[] args) {
        
    }
    public void rotate(int[] nums, int k) {
            //if zero or one element no rotation 
            if(nums.length==0 || nums.length==1)return ; 
            //handle if k>n
            k=k%nums.length;
            //reverse 0 - n
            reverse(nums, 0, nums.length-1);
            reverse(nums, 0, k-1);
            reverse(nums, k, nums.length-1);
    }

    public static void reverse(int[] nums, int s, int e){
        int start = s , end = e; 
        while(start<end){   
            int temp = nums[start];
            nums[start]=nums[end];
            nums[end]= temp;
             start++; 
             end--;
        }
    }
}