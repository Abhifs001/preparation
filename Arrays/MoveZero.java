public class MoveZero {
      public static void main(String[] args) {

        int [] nums = {0,1,0,3,12};

        int ans[]  = new int[nums.length];

        for(int i =0;i<nums.length;i++){
            if(nums[i]!=0){
                ans[i]=nums[i];
            } 
        }
       
        
        for(int i = 0 ; i < nums.length;i++){
            System.out.println(ans[i]);
        }
        for(int i = 0 ; i < nums.length;i++){
            nums[i]=ans[i];
        }

        
    }
}
